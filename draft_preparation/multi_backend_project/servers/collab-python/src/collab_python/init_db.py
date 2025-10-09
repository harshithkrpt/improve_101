# init_db.py
from db import get_conn

CREATE_USERS = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);
"""

with get_conn() as conn:
    with conn.cursor() as cur:
        cur.execute(CREATE_USERS)
    # conn.commit() not needed inside context manager unless you prefer explicit
print("tables created")
