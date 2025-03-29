import { validationRequestBody } from "@/middleware/validationRequest";
import User from "@/models/User/User";
import { logger } from "@/utils/logger";
import { userSchema } from "@/utils/validations/schemaValidators";
import express, { Request, Response, Router } from "express";
const router: Router = express.Router();
import bcrypt from "bcrypt";
import { generateJwtToken } from "@/utils/common";
import { validateToken } from "@/middleware/authentication";

/*
    path: v1/user/:userId
    method: get
*/
router.get("/:userId", validateToken  ,async (request: Request, response: Response) => {
  const userId = request.params.userId;
  try {
    const userDetails = await User.findOne({
      username: userId,
    });

    if (userDetails) {
      logger.info("User Found");
      response.json({
        data: {
          username: userDetails.username,
          email: userDetails.email,
          firstName: userDetails.firstName,
          lastName: userDetails.lastName ?? null,
          phone: userDetails.phone ?? null,
          address: userDetails.address ?? null,
          city: userDetails.city ?? null,
          state: userDetails.state ?? null,
          country: userDetails.country ?? null,
        },
        success: true,
      });
    } else {
      logger.info("User Not Found");
      response.status(404).json({
        message: "User Not Found",
      });
    }
  } catch (err) {
    logger.error(err);
  }
});

router.post("/signup", async (request: Request, response: Response) => {
  const { username, email, password, firstName } = request.body;

  try {
    const hashedPassword = await bcrypt.hash(password, 10);
    const userExists = await User.findOne({
      username,
    });

    if (userExists) {
      logger.info("User Already Exists");
      response.status(400).json({
        message: "User Already Exists",
        success: false,
      });
      return;
    }

    const userData = new User({
      username,
      email,
      password: hashedPassword,
      firstName,
    });
    await userData.save();
    logger.info("User Created Successfully");
    logger.info(`username: ${username}, email: ${email}`);
    logger.info(`----------------------------------------`);
    response.status(200).json({
      message: "User Created Successfully",
      success: true,
    });
  } catch (err) {
    logger.error(err);
  }
});

// Create a login route with jwt
router.post("/login", async (request: Request, response: Response) => {
  const { username, password } = request.body;
  try {
    const user = await User.findOne({
      username,
    });

    if (!user) {
      logger.info("User Not Found");
      response.status(404).json({
        message: "User Not Found",
        success: false,
      });
      return;
    }

    const isPasswordValid = await bcrypt.compare(password, user.password);

    if (!isPasswordValid) {
      logger.info("Invalid Password");
      response.status(401).json({
        message: "Invalid Password",
        success: false,
      });
      return;
    }

    // Generate JWT
    const jwtToken = generateJwtToken({
      username: user.username,
      email: user.email,
    });
    logger.info("JWT Token Generated");
    response.status(200).json({
      message: "User Logged In Successfully",
      success: true,
      token: jwtToken,
    });
  } catch (err) {
    logger.error(err);
    response.status(500).json({
      success: false,
      message: "Internal Server Error",
      error: err.message,
    });
  }
});

export default router;
