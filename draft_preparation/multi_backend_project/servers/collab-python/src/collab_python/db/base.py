from dotenv import load_dotenv
import os
import psycopg
from contextlib import contextmanager

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

@contextmanager
def get_conn():
    # psycopg.Connection used in "autocommit=False" by default
    with psycopg.connect(DATABASE_URL) as conn:
        yield conn