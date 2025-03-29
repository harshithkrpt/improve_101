"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const dotenv_1 = __importDefault(require("dotenv"));
const mongoose_1 = __importDefault(require("mongoose"));
const logger_1 = require("@utils/logger");
const userRoute_1 = __importDefault(require("@routes/userRoute"));
const express_rate_limit_1 = __importDefault(require("express-rate-limit"));
const express_slow_down_1 = __importDefault(require("express-slow-down"));
dotenv_1.default.config();
const port = Number(process.env.PORT || "3000");
const mongoURI = process.env.MONGO_URI;
const app = (0, express_1.default)();
// Middleware
app.use(express_1.default.json());
// Speed Limiter
app.use((0, express_slow_down_1.default)({
    windowMs: 15 * 60 * 1000,
    delayAfter: 20,
    delayMs: () => 2000,
}));
// Rate Limiting
app.use((0, express_rate_limit_1.default)({
    windowMs: 15 * 60 * 1000,
    max: 50,
    message: "Too many requests from this IP, please try again later.",
}));
// Routes
app.get("/", (req, res) => {
    res.status(200).send("Server is running!");
});
app.use("/v1/user", userRoute_1.default);
// MongoDB Connection and Server Start
mongoose_1.default
    .connect(mongoURI)
    .then(() => {
    logger_1.logger.info("✅ MongoDB Connected");
    app.listen(port, () => {
        logger_1.logger.info(`🚀 [server]: Server is running at http://localhost:${port}`);
    });
})
    .catch((err) => {
    logger_1.logger.error("❌ MongoDB Connection Failed", err);
    process.exit(1); // Exit the process if DB connection fails
});
