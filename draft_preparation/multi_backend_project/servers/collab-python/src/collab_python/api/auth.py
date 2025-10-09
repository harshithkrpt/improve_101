from fastapi import HTTPException, APIRouter
from collab_python.schemas.user import UserRequestSignUp,UserLoginRequest
from collab_python.db.base import get_conn
from collab_python.util.common import hash_password, is_valid_password, generate_jwt
from psycopg import errors, rows


router = APIRouter(prefix="/api/v1/auth", tags=["Auth Routes"])

@router.post('/signup')
def add_user(user_request: UserRequestSignUp):
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
def login_user(login_request: UserLoginRequest):
    with get_conn() as conn:
        with conn.cursor(row_factory=rows.dict_row) as cur:
            # fetch the user 
            cur.execute("SELECT email, password_hash, display_name FROM users WHERE email = %s", (login_request.username, ))
            user = cur.fetchone()
            if user is None:
                raise HTTPException(status_code=400, detail='Invalid Credentials') 
            print(user, "added user", user.get("email"))
            is_valid = is_valid_password(login_request.password, hashed=user.get('password_hash'))
            if is_valid == False:
                raise HTTPException(status_code=400, detail='Invalid Credentials') 
            
            # now generate the jwt by adding username, email
            jwt_token = generate_jwt(payload={'email': user.get('email')})
            return {
                'token': jwt_token
            }
