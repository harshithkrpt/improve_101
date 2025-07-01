import { NextFunction, Request, Response } from 'express';
import jwt from 'jsonwebtoken';
import dotenv from 'dotenv';

dotenv.config();


export const validateToken = (request: Request, response: Response, next: NextFunction) => {
    const authHeader = request.headers.authorization;

    if (authHeader) {
        const token = authHeader.split(' ')[1];

        jwt.verify(token, process.env.HASH_SECRET, (err, payload) => {
            if(err) {
                response.status(403).json({
                    success: false, 
                    message: 'Invalid token',
                })
            }
            else {
                request["user"] = payload;
                next();
            }
        })
    }
    else {
        response.status(401).json({
            success: false,
            message: 'Token is not provided',
        });
    }
}