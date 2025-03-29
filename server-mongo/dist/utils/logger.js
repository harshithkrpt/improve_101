"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.logger = void 0;
const winston_1 = __importDefault(require("winston"));
const dotenv_1 = __importDefault(require("dotenv"));
dotenv_1.default.config();
exports.logger = winston_1.default.createLogger({
    level: process.env.LOG_LEVEL || "info",
    format: winston_1.default.format.simple(),
    transports: [
        new winston_1.default.transports.Console(),
        new winston_1.default.transports.File({
            filename: process.env.LOG_FILE || "error.log",
            level: process.env.LOG_LEVEL || "info",
        }),
    ],
});
