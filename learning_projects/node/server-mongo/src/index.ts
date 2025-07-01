import express, { Request, Response, Express } from "express";
import dotenv from "dotenv";
import mongoose from "mongoose";
import { logger } from "@utils/logger";
import userRoute from "@routes/userRoute";
import rateLimit from "express-rate-limit";
import slowDown from "express-slow-down";

dotenv.config();

const port: number = Number(process.env.PORT || "3000");
const mongoURI: string = process.env.MONGO_URI as string;

const app: Express = express();

// Middleware
app.use(express.json());

// Speed Limiter
app.use(slowDown({
  windowMs: 15 * 60 * 1000,
  delayAfter: 20,
  delayMs: () => 2000,
}));

// Rate Limiting
app.use(rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 50,
  message: "Too many requests from this IP, please try again later.",
}));



// Routes
app.get("/", (req: Request, res: Response) => {
  res.status(200).send("Server is running!");
});

app.use("/v1/user", userRoute);

// MongoDB Connection and Server Start
mongoose
  .connect(mongoURI)
  .then(() => {
    logger.info("✅ MongoDB Connected");

    app.listen(port, () => {
      logger.info(`🚀 [server]: Server is running at http://localhost:${port}`);
    });
  })
  .catch((err) => {
    logger.error("❌ MongoDB Connection Failed", err);
    process.exit(1); // Exit the process if DB connection fails
  });
