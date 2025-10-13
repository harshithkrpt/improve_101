from collab_python.db.base import get_conn
from psycopg import rows
# TODO: Fix this below package properly without psycopg2-binary
from psycopg2.extras import execute_values
import logging
from collab_python.schemas.list import ListDaoIn
# api dao for fetch data
from collab_python.schemas.list import UpdateListIn, BookMarkListIn

def fetch_my_lists(owner_id: int, offset:int = 0, limit = 10):
    with get_conn() as conn:
        with conn.cursor(row_factory=rows.dict_row) as cur:
            try:
                QUERY = """
                 SELECT 
                    li.id, 
                    li.title, 
                    li.description, 
                    li.created_at, 
                    li.updated_at, 
                    li.owner_id,
                    usr.display_name
                    FROM lists li 
                    INNER JOIN users usr ON 
                    usr.id = li.owner_id
                    WHERE li.owner_id = %s
                    LIMIT %s 
                    OFFSET %s
                """
                cur.execute(QUERY, (owner_id, limit, offset))
                res = cur.fetchall()
                print(res)
                return res
            except Exception as ex:
                logging.error(ex)

           

def add_list(input: ListDaoIn, public: bool = False):
    with get_conn() as conn:
        with conn.cursor() as cur:
            try:
                QUERY = """
                INSERT INTO lists(title, description, owner_id, is_public) VALUES (
                    %s,
                    %s,
                    %s,
                    %s
                ) RETURNING id;
                """
                cur.execute(QUERY, (input.title, input.description, input.owner_id, public))
                res = cur.fetchone()
                if res:
                 return True
            except Exception as ex:
                logging.error(ex)


def delete_list(list_id: int):
    with get_conn() as conn:
        with conn.cursor() as cur:
            try:
                QUERY = """
                DELETE FROM lists WHERE id = %s RETURNING id;
                """
                cur.execute(QUERY, (list_id, ))
                res = cur.fetchone()
                if res:
                    return True
            except Exception as ex:
                logging.error(ex)

def owner_of_list(list_id: int):
    with get_conn() as conn:
        with conn.cursor(row_factory=rows.dict_row) as cur:
            try:
                QUERY = """
                SELECT owner_id FROM lists WHERE id = %s
                """
                cur.execute(QUERY, (list_id, ))
                res = cur.fetchone()
                logging.info(res)
                return res.get("owner_id")
            except Exception as ex:
                logging.error(ex)


def fetch_list_id(list_id: int, get_minimal_info = False):
    with get_conn() as conn:
        with conn.cursor(row_factory=rows.dict_row) as cur:
            try:
                QUERY = ""
                if not get_minimal_info:
                    QUERY = """
                    SELECT 
                        li.id, 
                        li.title, 
                        li.description, 
                        li.created_at, 
                        li.updated_at, 
                        li.owner_id,
                        usr.display_name
                        FROM lists li 
                        INNER JOIN users usr ON 
                        usr.id = li.owner_id
                        WHERE li.id = %s
                    """
                else:
                    QUERY = """
                    SELECT 
                        li.id,
                        li.owner_id,
                        li.description,
                        li.title,
                        li.is_public
                        FROM lists li WHERE li.id = %s
                    """
                cur.execute(QUERY, (list_id, ))
                res = cur.fetchone()
                return res
                
            except Exception as ex:
                logging.error(ex)


def update_list_id(list_item: UpdateListIn):
    with get_conn() as conn:
        with conn.cursor() as cur:
            try:
                QUERY = """
                UPDATE lists
                SET title = %s,
                    description = %s,
                    is_public = %s
                WHERE id = %s
                """
                cur.execute(QUERY, (list_item.get("title"), list_item.get("description"), list_item.get("is_public"), list_item.get("id")))        
                return True
            except Exception as ex:
                logging.error(ex)



def add_bookmark_to_list_repo(list_id: int, bookmark_in: BookMarkListIn):
    with get_conn() as conn:
        bookmark = ""
        with conn.cursor() as cur:
            try:
                QUERY = """
                    INSERT INTO 
                        bookmarks(list_id, url, title, notes, read)
                    VALUES 
                    (%s, %s, %s, %s, %s) RETURNING id, url, title, notes, read;
                """
                cur.execute(QUERY, (list_id, bookmark_in.url, bookmark_in.title, bookmark_in.notes, bookmark_in.read))
                bookmark = cur.fetchone()
            except Exception as ex:
                logging.error(ex)
        if not len(bookmark_in.tags):
            return { "bookmark" : bookmark}

        # insert into tags
        with conn.cursor() as cur:
           try:
                tags = [(n,) for n in bookmark_in.tags]
                QUERY = """
                    WITH new_tags(name) AS (VALUES %s),
                    ins AS (
                        INSERT INTO tags(name)
                        SELECT name FROM new_tags nt WHERE NOT EXISTS (
                            SELECT 1 FROM tags t WHERE t.name = nt.name
                        )
                        RETURNING id, name
                    )
                    SELECT id, name
                    FROM tags 
                    WHERE name IN (SELECT name FROM new_tags);
                """
                execute_values(cur, QUERY, tags)
                inserted_tags = cur.fetchall()
                
                QUERY_FOR_LINKING = """
                    INSERT INTO 
                        bookmark_tags(bookmark_id, tag_id) 
                    VALUES %s ON CONFLICT DO NOTHING;
                """
                # Normalize bookmark id extraction (works for tuple or dict-row)
                if isinstance(bookmark, (list, tuple)):
                    bookmark_id = bookmark[0]
                elif isinstance(bookmark, dict):
                    bookmark_id = bookmark.get("id")
                else:
                    # try attribute-style
                    bookmark_id = getattr(bookmark, "id", None)

                if bookmark_id is None:
                    raise RuntimeError("could not determine inserted bookmark id")

                # Prepare linking rows (bookmark_id, tag_id)
                # tags_rows might be list of tuples (id, name) or list of dicts
                linking_values = []
                for r in inserted_tags:
                    if isinstance(r, (list, tuple)):
                        tag_id = r[0]
                    elif isinstance(r, dict):
                        tag_id = r.get("id")
                    else:
                        tag_id = getattr(r, "id", None)
                    if tag_id is None:
                        raise RuntimeError("could not determine tag id from inserted_tags")
                    linking_values.append((bookmark_id, tag_id))
                execute_values(cur, QUERY_FOR_LINKING, linking_values)
                return {
                    "bookmark": bookmark,
                    "tags": inserted_tags
                }
           except Exception as exp:
               logging.error(exp)

        return bookmark