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
Object.defineProperty(exports, "__esModule", { value: true });
exports.validationRequestBody = void 0;
const validationRequestBody = (schema) => __awaiter(void 0, void 0, void 0, function* () {
    return (req, res, next) => __awaiter(void 0, void 0, void 0, function* () {
        const body = req.body;
        const validation = schema.validate(body, { abortEarly: false });
        if (validation.error) {
            return res.status(400).json({
                success: false,
                errors: validation.error.details.map((detail) => detail.message)
            });
        }
        next();
    });
});
exports.validationRequestBody = validationRequestBody;
