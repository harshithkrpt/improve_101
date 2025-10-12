from fastapi import HTTPException, APIRouter, Request, Depends
from collab_python.schemas.user import UserRequestSignUp,UserLoginRequest, RefreshRequest
from collab_python.util.common import hash_password, is_valid_password, generate_login_response, cleanup_login_payload, decode_jwt, generate_access_jwt,get_currenttimestamp, validate_token
import collab_python.repository.user as user_repository
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

router = APIRouter(prefix="/api/v1/auth", tags=["Auth Routes"])

@router.post('/signup')
# TODO: Add Validation from Pydantic
async def add_user(user_request: UserRequestSignUp):
    user_request.password = hash_password(user_request.password)
    result = await asyncio.to_thread(user_repository.insert_user, user_request)
    return result

@router.post("/login")
async def login_user(login_request: UserLoginRequest, request: Request):
    redis = request.app.state.redis 
    user = await asyncio.to_thread(user_repository.fetch_user, login_request.username, True)
    if user is None:
        raise HTTPException(status_code=400, detail='Invalid Credentials') 
    is_valid = is_valid_password(login_request.password, hashed=user.get('password_hash'))
    if is_valid == False:
        raise HTTPException(status_code=400, detail='Invalid Credentials') 
    cleanup_login_payload(user)
  
    key = f"user::refresh::{user.get('id')}"
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
        

# TODO: Fix this api as the token generated does not have same keys as generated via login
@router.post('/refresh_access')
async def refresh_access(body: RefreshRequest, request: Request):
    redis = request.app.state.redis
    decoded_jwt = decode_jwt(body.refresh_token)
    user_id = decoded_jwt.get("id")
    redis_key = f"user::refresh::{user_id}"
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
    username = payload.get("sub")
    res = await asyncio.to_thread(user_repository.fetch_user, username)
    return res