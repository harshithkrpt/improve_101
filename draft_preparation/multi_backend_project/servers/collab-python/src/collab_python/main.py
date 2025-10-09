# src/collab_python/main.py
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from collab_python.db import get_conn
from psycopg import errors

class UserIn(BaseModel):
    name: str
    email: str | None = None


app = FastAPI(title='Collab')


@app.post('/users', status_code = 201)
def create_user(user: UserIn):
    INSERT = "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id, name, email, created_at"
    with get_conn() as con:
        with con.cursor() as cur:
            try:
                cur.execute(INSERT, (user.name, user.email,))
                res = cur.fetchone()
                return res
            except errors.UniqueViolation:
               
                raise HTTPException(status_code = 400, detail = "email already exists")



@app.get("/users")
def get_all_users(limit:int = 100):
    
    QUERY = 'SELECT * from users LIMIT %s'
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(QUERY, (limit, ))
            rows = cur.fetchall()
            return rows

@app.get("/users/{user_id}")
def get_user(user_id: int):
    QUERY = "SELECT id, name, email, created_at FROM users WHERE id = %s "
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(QUERY, (user_id,))
            result = cur.fetchone()
            if result is None:
                raise HTTPException(status_code = 404, detail='User is not found')
            return dict(result)

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    DELETE = "DELETE FROM users WHERE id = %s RETURNING id;"
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(DELETE, (user_id,))
            if cur.fetchone() is None:
                raise HTTPException(status_code=404, detail="not found")
    return {}


@app.get("/")
def read_root():
    return {"message": "Hello from collab-python!"}

def start() -> None:
    uvicorn.run("collab_python.main:app", host="localhost", port=8002, reload=True)

if __name__ == "__main__":
    start()
