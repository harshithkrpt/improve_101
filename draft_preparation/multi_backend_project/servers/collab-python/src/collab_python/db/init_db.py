# init_db.py
from db.base import get_conn

CREATE_USERS = """
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  display_name TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now(),
  last_seen TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS lists (
  id SERIAL PRIMARY KEY,
  owner_id INTEGER NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  is_public BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  CONSTRAINT fk_lists_owner FOREIGN KEY (owner_id)
    REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS bookmarks (
  id SERIAL PRIMARY KEY,
  list_id INTEGER NOT NULL,
  url TEXT NOT NULL,
  title TEXT NOT NULL,
  notes TEXT,
  favicon_url TEXT,
  read BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  CONSTRAINT fk_bookmarks_list FOREIGN KEY (list_id)
    REFERENCES lists(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tags (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS bookmark_tags (
  bookmark_id INTEGER NOT NULL,
  tag_id INTEGER NOT NULL,
  PRIMARY KEY (bookmark_id, tag_id),
  CONSTRAINT fk_bt_bookmark FOREIGN KEY (bookmark_id)
    REFERENCES bookmarks(id) ON DELETE CASCADE,
  CONSTRAINT fk_bt_tag FOREIGN KEY (tag_id)
    REFERENCES tags(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS comments (
  id SERIAL PRIMARY KEY,
  bookmark_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  body TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now(),
  CONSTRAINT fk_comments_bookmark FOREIGN KEY (bookmark_id)
    REFERENCES bookmarks(id) ON DELETE CASCADE,
  CONSTRAINT fk_comments_user FOREIGN KEY (user_id)
    REFERENCES users(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS collaborators (
  list_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  role TEXT CHECK (role IN ('owner', 'editor', 'viewer')) DEFAULT 'viewer',
  PRIMARY KEY (list_id, user_id),
  CONSTRAINT fk_collab_list FOREIGN KEY (list_id)
    REFERENCES lists(id) ON DELETE CASCADE,
  CONSTRAINT fk_collab_user FOREIGN KEY (user_id)
    REFERENCES users(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS analytics (
  id SERIAL PRIMARY KEY,
  entity_type TEXT NOT NULL,
  entity_id INTEGER,
  event_type TEXT NOT NULL,
  metadata JSONB,
  created_at TIMESTAMPTZ DEFAULT now()
);
"""

with get_conn() as conn:
    with conn.cursor() as cur:
        cur.execute(CREATE_USERS)
    # conn.commit() not needed inside context manager unless you prefer explicit
print("tables created")
