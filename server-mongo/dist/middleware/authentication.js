"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.validateToken = void 0;
const jsonwebtoken_1 = __importDefault(require("jsonwebtoken"));
const dotenv_1 = __importDefault(require("dotenv"));
dotenv_1.default.config();
const validateToken = (request, response, next) => {
    const authHeader = request.headers.authorization;
    if (authHeader) {
        const token = authHeader.split(' ')[1];
        jsonwebtoken_1.default.verify(token, process.env.HASH_SECRET, (err, payload) => {
            if (err) {
                response.status(403).json({
                    success: false,
                    message: 'Invalid token',
                });
            }
            else {
                request["user"] = payload;
                next();
            }
        });
    }
    else {
        response.status(401).json({
            success: false,
            message: 'Token is not provided',
        });
    }
};
exports.validateToken = validateToken;
