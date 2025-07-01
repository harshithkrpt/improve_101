"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const User_1 = __importDefault(require("@/models/User/User"));
const logger_1 = require("@/utils/logger");
const express_1 = __importDefault(require("express"));
const router = express_1.default.Router();
const bcrypt_1 = __importDefault(require("bcrypt"));
const common_1 = require("@/utils/common");
const authentication_1 = require("@/middleware/authentication");
/*
    path: v1/user/:userId
    method: get
*/
router.get("/:userId", authentication_1.validateToken, (request, response) => __awaiter(void 0, void 0, void 0, function* () {
    var _a, _b, _c, _d, _e, _f;
    const userId = request.params.userId;
    try {
        const userDetails = yield User_1.default.findOne({
            username: userId,
        });
        if (userDetails) {
            logger_1.logger.info("User Found");
            response.json({
                data: {
                    username: userDetails.username,
                    email: userDetails.email,
                    firstName: userDetails.firstName,
                    lastName: (_a = userDetails.lastName) !== null && _a !== void 0 ? _a : null,
                    phone: (_b = userDetails.phone) !== null && _b !== void 0 ? _b : null,
                    address: (_c = userDetails.address) !== null && _c !== void 0 ? _c : null,
                    city: (_d = userDetails.city) !== null && _d !== void 0 ? _d : null,
                    state: (_e = userDetails.state) !== null && _e !== void 0 ? _e : null,
                    country: (_f = userDetails.country) !== null && _f !== void 0 ? _f : null,
                },
                success: true,
            });
        }
        else {
            logger_1.logger.info("User Not Found");
            response.status(404).json({
                message: "User Not Found",
            });
        }
    }
    catch (err) {
        logger_1.logger.error(err);
    }
}));
router.post("/signup", (request, response) => __awaiter(void 0, void 0, void 0, function* () {
    const { username, email, password, firstName } = request.body;
    try {
        const hashedPassword = yield bcrypt_1.default.hash(password, 10);
        const userExists = yield User_1.default.findOne({
            username,
        });
        if (userExists) {
            logger_1.logger.info("User Already Exists");
            response.status(400).json({
                message: "User Already Exists",
                success: false,
            });
            return;
        }
        const userData = new User_1.default({
            username,
            email,
            password: hashedPassword,
            firstName,
        });
        yield userData.save();
        logger_1.logger.info("User Created Successfully");
        logger_1.logger.info(`username: ${username}, email: ${email}`);
        logger_1.logger.info(`----------------------------------------`);
        response.status(200).json({
            message: "User Created Successfully",
            success: true,
        });
    }
    catch (err) {
        logger_1.logger.error(err);
    }
}));
// Create a login route with jwt
router.post("/login", (request, response) => __awaiter(void 0, void 0, void 0, function* () {
    const { username, password } = request.body;
    try {
        const user = yield User_1.default.findOne({
            username,
        });
        if (!user) {
            logger_1.logger.info("User Not Found");
            response.status(404).json({
                message: "User Not Found",
                success: false,
            });
            return;
        }
        const isPasswordValid = yield bcrypt_1.default.compare(password, user.password);
        if (!isPasswordValid) {
            logger_1.logger.info("Invalid Password");
            response.status(401).json({
                message: "Invalid Password",
                success: false,
            });
            return;
        }
        // Generate JWT
        const jwtToken = (0, common_1.generateJwtToken)({
            username: user.username,
            email: user.email,
        });
        logger_1.logger.info("JWT Token Generated");
        response.status(200).json({
            message: "User Logged In Successfully",
            success: true,
            token: jwtToken,
        });
    }
    catch (err) {
        logger_1.logger.error(err);
        response.status(500).json({
            success: false,
            message: "Internal Server Error",
            error: err.message,
        });
    }
}));
exports.default = router;
