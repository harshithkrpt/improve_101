import jwt 
from dotenv import load_dotenv
import os
from passlib.hash import argon2
from datetime import datetime, timezone , timedelta
load_dotenv()
import uuid

def _get_username(payload: dict):
    # support dict or object with .username
    if isinstance(payload, dict):
        return payload.get("username") or payload.get("email") or payload.get("sub")
    return getattr(payload, "username", None) or getattr(payload, "email", None)


def generate_jwt(payload: dict, token_type = 'access', expiry_delta_minutes = 20, jti: str = ''):
    secret = os.getenv('JWT_SECRET') 
    if not secret:
        raise RuntimeError("JWT_SECRET environment variable is not set")
    now_dt = datetime.now(timezone.utc)
    exp_dt = now_dt + timedelta(minutes=expiry_delta_minutes)
    username = _get_username(payload)
    if not username:
        raise ValueError("payload must contain a username/email/sub")

    new_payload = {
        'sub': username,
        'iat': int(now_dt.timestamp()), # issued timestamp
        'exp': int(exp_dt.timestamp()), # expiry timestamp
        'iss': 'collab',
        'type': token_type,
        'jti': jti
    }

    token = jwt.encode(new_payload, secret, algorithm="HS256")
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    return token

def generate_access_jwt(payload, jti):
    return generate_jwt(payload, 'access', expiry_delta_minutes=20, jti=jti)

def generate_refresh_jwt(payload, jti):
    return generate_jwt(payload, 'refresh', expiry_delta_minutes=2 * 24 * 60, jti=jti)

def decode_jwt(jwt_tokwn: str):
    secret = os.getenv('JWT_SECRET')
    return jwt.decode(jwt_tokwn, secret, algorithm='HS256')

def cleanup_login_payload(payload: dict):
    del payload['password_hash']

def generate_login_response(payload: dict):
    jti = str(uuid.uuid4())
   
    try:
        login_response = {
            'jti': jti,
            'access_token': generate_access_jwt(payload=payload, jti=jti),
            'refresh_token': generate_refresh_jwt(payload=payload, jti=jti),
            'expires_in': 20 * 60,
            "user": payload
        }

        return login_response
    except Exception:
        return {}

    


def hash_password(current_password: str):
    return argon2.hash(current_password)

def is_valid_password(current_password: str, hashed: str):
    return argon2.verify(current_password, hashed)