import jwt 
from dotenv import load_dotenv
import os
from passlib.hash import argon2
from datetime import datetime, timezone , timedelta
load_dotenv()
import uuid
from fastapi import HTTPException, Request
from jwt import InvalidTokenError, ExpiredSignatureError
import json
import logging

def _get_username(payload: dict):
    # TODO: You use various fields (username, email, sub) in _get_username. Good flexibility — but be consistent: set sub to user id (or email) and in refresh use that consistently. Prefer using immutable id (user_id) in sub if you want to support email changes.
    # support dict or object with .username
    if isinstance(payload, dict):
        return payload.get("username") or payload.get("email") or payload.get("sub")
    return getattr(payload, "username", None) or getattr(payload, "email", None)


def generate_jwt(payload: dict, token_type = 'access', expiry_delta_minutes = 20, jti: str = None):
    if jti is None:
        jti = str(uuid.uuid4())

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
        'jti': jti,
        'id': payload.get("id")
    }

    token = jwt.encode(new_payload, secret, algorithm=os.getenv("JWT_ALGORITHM"))
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    return token

def generate_access_jwt(payload, jti):
    return generate_jwt(payload, 'access', expiry_delta_minutes=20, jti=jti)

def generate_refresh_jwt(payload, jti):
    # TODO: Refresh token expiry and Redis TTL should match
    return generate_jwt(payload, 'refresh', expiry_delta_minutes=2 * 24 * 60, jti=jti)

def validate_token(request: Request):
    auth = request.headers.get("Authorization")

    if not auth:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    if not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization header format")

    token = auth.split(" ")[1]

    return decode_jwt(token)

def decode_jwt(jwt_token: str) -> dict:
    secret = os.getenv('JWT_SECRET')
    if not secret:
        raise RuntimeError("JWT_SECRET environment variable is not set")
    try:
        return jwt.decode(jwt_token, secret, algorithms=[os.getenv("JWT_ALGORITHM")])
    except ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token Expired")
    except InvalidTokenError:
        raise HTTPException(status_code=400, detail="Invalid Token")

def cleanup_login_payload(payload: dict):
    payload.pop('password_hash', None)

def generate_login_response(payload: dict, refresh: bool = None):
    jti_access = str(uuid.uuid4())
    jti_refresh = str(uuid.uuid4())

    try:
        login_response = {
            'jti': jti_access,
            'access_token': generate_access_jwt(payload=payload, jti=jti_access),
            'refresh_token':  generate_refresh_jwt(payload=payload, jti=jti_refresh) if refresh is None else refresh,
            'expires_in': 20 * 60,
            "user": payload,
            "tokenType": "Bearer"
        }

        return login_response
    except Exception as e:
        logging.error(f"Failed to build login response , {e}")
        raise RuntimeError("Internal error generating tokens")
    
def get_currenttimestamp() -> int:
    return int(datetime.now(timezone.utc).timestamp())


def hash_password(current_password: str):
    return argon2.hash(current_password)

def is_valid_password(current_password: str, hashed: str):
    return argon2.verify(current_password, hashed)