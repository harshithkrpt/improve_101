from collab_python.db.base import get_conn
from psycopg import rows
import logging
from collab_python.schemas.list import ListDaoIn
# api dao for fetch data
from collab_python.schemas.list import UpdateListIn

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