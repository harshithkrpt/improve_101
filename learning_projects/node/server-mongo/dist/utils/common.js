"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.generateJwtToken = void 0;
const jsonwebtoken_1 = __importDefault(require("jsonwebtoken"));
const dotenv_1 = __importDefault(require("dotenv"));
dotenv_1.default.config();
// 🔹 Ensure HASH_SECRET is properly set
const HASH_SECRET = process.env.HASH_SECRET;
if (!HASH_SECRET) {
    throw new Error("HASH_SECRET is not defined in .env");
}
const generateJwtToken = (payload) => {
    const secretKey = HASH_SECRET;
    const token = jsonwebtoken_1.default.sign(payload, secretKey, {
        expiresIn: '1h'
    });
    return token;
};
exports.generateJwtToken = generateJwtToken;
