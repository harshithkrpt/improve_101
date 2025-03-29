import jwt from "jsonwebtoken";

import dotenv from "dotenv";


dotenv.config();

// 🔹 Ensure HASH_SECRET is properly set
const HASH_SECRET = process.env.HASH_SECRET;
if (!HASH_SECRET) {
  throw new Error("HASH_SECRET is not defined in .env");
}



export const generateJwtToken = (payload: object) => {
    const secretKey = HASH_SECRET;

    const token = jwt.sign(payload, secretKey, {
        expiresIn: '1h'
    });

    return token;
}