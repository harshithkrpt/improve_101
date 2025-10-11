
from collab_python.db.base import get_conn
from collab_python.schemas.user import UserRequestSignUp
from psycopg import rows, errors
from fastapi import HTTPException

def fetch_user(username, return_password = False):
    with get_conn() as conn:
        with conn.cursor(row_factory=rows.dict_row) as cur:
            res = None
            if not return_password:
                cur.execute("SELECT email, id, display_name FROM users WHERE email = %s", (username,))
                res = cur.fetchone()
            else:
                cur.execute("SELECT email, password_hash, display_name, id FROM users WHERE email = %s", (username, ))
                res = cur.fetchone()
            if res is None:
                raise HTTPException(status_code=404, detail=f"{username} is not found.")
            else:
                return res

def insert_user(user: UserRequestSignUp):
    with get_conn() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO users(email, display_name, password_hash) VALUES (%s, %s, %s) RETURNING id, display_name, email, created_at", 
                    (user.email, user.display_name, user.password)
                )
                return { 
                    "message": "User Created Successfully."
                }
            except errors.UniqueViolation:
                raise HTTPException(status_code=400, detail="email already exists")
