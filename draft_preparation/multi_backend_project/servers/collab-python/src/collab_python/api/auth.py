from fastapi import HTTPException, APIRouter, Request, Depends
from collab_python.schemas.user import UserRequestSignUp,UserLoginRequest, RefreshRequest
from collab_python.db.base import get_conn
from collab_python.util.common import hash_password, is_valid_password, generate_login_response, cleanup_login_payload, decode_jwt, generate_access_jwt,get_currenttimestamp, validate_token
from psycopg import errors, rows

import logging

logging.basicConfig(level=logging.INFO)

router = APIRouter(prefix="/api/v1/auth", tags=["Auth Routes"])

@router.post('/signup')
async def add_user(user_request: UserRequestSignUp):
    # TODO: CHECK USER VALIDATIONS IF REQUIRED SEE IF WE CAN DO IN PYDANTIC
    with get_conn() as conn:
        with conn.cursor() as cur:
            try:
                hashed_password = hash_password(user_request.password)
                cur.execute(
                    "INSERT INTO users(email, display_name, password_hash) VALUES (%s, %s, %s) RETURNING id, display_name, email, created_at", 
                    (user_request.email, user_request.display_name, hashed_password)
                    ) 

                return { 
                    "message": "User Created Successfully."
                }
            except errors.UniqueViolation:
                raise HTTPException(status_code=400, detail="email already exists")

@router.post("/login")
async def login_user(login_request: UserLoginRequest, request: Request):
    redis = request.app.state.redis
    # TODO: Below is blocking I/O Move it to async
    with get_conn() as conn:
        with conn.cursor(row_factory=rows.dict_row) as cur:
            # fetch the user 
            cur.execute("SELECT email, password_hash, display_name, id FROM users WHERE email = %s", (login_request.username, ))
            user = cur.fetchone()
            if user is None:
                raise HTTPException(status_code=400, detail='Invalid Credentials') 
            is_valid = is_valid_password(login_request.password, hashed=user.get('password_hash'))
            if is_valid == False:
                raise HTTPException(status_code=400, detail='Invalid Credentials') 
            cleanup_login_payload(user)
            
            # store the redis if not exists
            # TODO: Using user.get('email') as the redis key ties refresh tokens to mutable data. Use user id (stable primary key) instead.
            key = f"user::refresh::{user.get('email')}"
            redis_refresh_token = await redis.get(key)
            
            response = generate_login_response(payload=user, refresh=redis_refresh_token)
        
            if redis_refresh_token is None:
                refresh_token = response.get("refresh_token")
                # TODO: When setting the refresh token convert to hashed form
                await redis.set(key, refresh_token, nx=True, ex=2 * 24 * 60 * 60)
            else:
                # TODO: When getting the refresh token from redis convert to normal/ raw form
                logging.info("Found refresh token in redis for user %s", user.get("email"))
                refresh_token = redis_refresh_token
            
            return response
        

@router.post('/refresh_access')
async def refresh_access(body: RefreshRequest, request: Request):
    redis = request.app.state.redis
    decoded_jwt = decode_jwt(body.refresh_token)
    username = decoded_jwt.get("sub")
    redis_key = f"user::refresh::{username}"
    redis_refresh_token = await redis.get(redis_key)
    now_dt = get_currenttimestamp()

    if redis_refresh_token is None:
        raise HTTPException(status_code=400, detail="Invalid Refresh Token")
    
    if decoded_jwt.get('type') != 'refresh':
        raise HTTPException(status_code=400, detail="Invalid Refresh Token")
    
    if now_dt > decoded_jwt.get("exp"):
        raise HTTPException(status_code=400, detail="Refresh Token Expired")
    
    if body.refresh_token != redis_refresh_token:
        raise HTTPException(status_code=400, detail="Refresh Tokens are not matching")

    # generate new access token
    return generate_access_jwt({
        'username': decoded_jwt.get("sub")
    }, jti=None)


@router.get("/me")
async def my_profile(payload: dict = Depends(validate_token)):
    
    with get_conn() as conn:
        with conn.cursor(row_factory=rows.dict_row) as cur:
            cur.execute("SELECT email, id, display_name FROM users WHERE email = %s", (payload.get("sub"),))
            res = cur.fetchone()
            if res is None:
                raise HTTPException(status_code=404, detail="Profile Information is Not Found")
            else:
                return res