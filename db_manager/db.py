import psycopg
from .config import DB_CONFIG
from db_manager.psql_queries import PSQL_QUERIES as psql
from enum import Enum, auto

config = DB_CONFIG

class Fetch(Enum):
    ONE = auto()
    ALL = auto()
    EXC = auto()

def execute(psql_raw, fetch: Fetch, params=None):
    try:
        with psycopg.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(psql_raw, params)

                if fetch == Fetch.ONE:
                    row = cur.fetchone()
                    return row
                elif fetch == Fetch.ALL:
                    rows = cur.fetchall()
                    return rows
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

def get_keywords_by_content_id(data):
    row = execute(psql.GET_KEYWORDS_BY_ID, Fetch.ONE, data)
    return row[0]

def get_unreviewed_keywords_ids():
    rows = execute(psql.GET_UNREVIEWED_KEYWORDS_IDS, Fetch.ALL)
    return rows

def get_content(data):
    row = execute(psql.GET_LESSON_CONTENT, Fetch.ONE, data)
    return row

def add_reviewed_keywords(data):
    execute(psql.INSERT_REVIEWED_KEYWORDS, Fetch.EXC, data)

def get_keywords_reviewed_bit(data):
    row = execute(psql.GET_KEYWORDS_REVIEWED_BIT, Fetch.ONE, data)
    return row[0]

def get_reviewed_keywords(data):
    row = execute(psql.GET_REVIEWED_KEYWORDS, Fetch.ONE, data)
    return row

def update_ai_keywords_reviewed_bit(data):
    execute(psql.UPDATE_AI_KEYWORDS_REVIEWED_BIT, Fetch.EXC, data)
