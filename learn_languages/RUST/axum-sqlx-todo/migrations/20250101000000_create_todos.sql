
-- 20250101000000_create_todos.sql

-- Migration to create the todos table
CREATE TABLE IF NOT EXISTS todos (
    id UUID PRIMARY KEY,
    TITLE TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
