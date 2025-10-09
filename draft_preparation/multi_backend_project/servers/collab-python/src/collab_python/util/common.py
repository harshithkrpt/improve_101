import jwt 
from dotenv import load_dotenv
import os
from passlib.hash import argon2

load_dotenv()

def generate_jwt(payload):
    secret = os.getenv('JWT_SECRET') 
    token = jwt.encode(payload, secret, algorithm="HS256")
    # PyJWT v2+ returns a str; if an older PyJWT returns bytes, coerce:
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    return token

def decode_jwt(jwt_tokwn: str):
    secret = os.getenv('JWT_SECRET')
    return jwt.decode(jwt_tokwn, secret, algorithm=['HS256'])



def hash_password(current_password: str):
    return argon2.hash(current_password)

def is_valid_password(current_password: str, hashed: str):
    return argon2.verify(current_password, hashed)