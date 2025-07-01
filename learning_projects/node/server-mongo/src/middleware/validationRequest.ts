import { NextFunction, Request, Response } from "express";
import { ObjectSchema } from "joi";

export const validationRequestBody = async (schema: ObjectSchema) => {
    return async (req: Request, res: Response, next: NextFunction) => {
            const body = req.body;
            const validation = schema.validate(body, { abortEarly: false });

            if(validation.error) {
                return res.status(400).json({
                    success: false,
                    errors: validation.error.details.map((detail: {message: string}) => detail.message)
                });
            }
            
            next();
    };
}