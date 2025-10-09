# src/collab_python/main.py
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from collab_python.db.base import get_conn
from psycopg import errors
import collab_python.api.auth as auth 

app = FastAPI(title='Collab')

app.include_router(auth.router)

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     QUERY = "SELECT id, name, email, created_at FROM users WHERE id = %s "
#     with get_conn() as conn:
#         with conn.cursor() as cur:
#             cur.execute(QUERY, (user_id,))
#             result = cur.fetchone()
#             if result is None:
#                 raise HTTPException(status_code = 404, detail='User is not found')
#             return result

# @app.delete("/users/{user_id}", status_code=204)
# def delete_user(user_id: int):
#     DELETE = "DELETE FROM users WHERE id = %s RETURNING id;"
#     with get_conn() as conn:
#         with conn.cursor() as cur:
#             cur.execute(DELETE, (user_id,))
#             if cur.fetchone() is None:
#                 raise HTTPException(status_code=404, detail="not found")
#     return {}


def start() -> None:
    uvicorn.run("collab_python.main:app", host="localhost", port=8002, reload=True)

if __name__ == "__main__":
    start()
