import winston, { Logger } from "winston";

import dotenv from "dotenv";
dotenv.config();

export const logger: Logger = winston.createLogger({
  level: process.env.LOG_LEVEL || "info",
  format: winston.format.simple(),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({
      filename: process.env.LOG_FILE || "error.log",
      level: process.env.LOG_LEVEL || "info",
    }),
  ],
});
