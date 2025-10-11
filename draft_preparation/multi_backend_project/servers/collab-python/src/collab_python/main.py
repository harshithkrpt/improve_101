
from fastapi import FastAPI
import uvicorn
import collab_python.api.auth as auth
import collab_python.api.lists as lists 
import redis.asyncio as redis
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title='Collab')

app.include_router(auth.router)
app.include_router(lists.router)

@app.on_event("startup")
async def app_start():
    app.state.redis = redis.from_url(os.getenv('REDIS_URL'), decode_responses=True)

@app.on_event("shutdown")
async def app_stop():
    await app.state.redis.close()

def start() -> None:
    uvicorn.run("collab_python.main:app", host="localhost", port=8002, reload=True)

if __name__ == "__main__":
    start()
