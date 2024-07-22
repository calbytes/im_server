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

def get_ai_keywords(data):
    row = execute(psql.GET_AI_KEYWORDS, Fetch.ONE, data)
    return row[0]

def get_reviewed_keywords(data):
    row = execute(psql.GET_REVIEWED_KEYWORDS, Fetch.ONE, data)
    return row[0]

def get_lesson_content(data):
    row = execute(psql.GET_LESSON_CONTENT, Fetch.ONE, data)
    return row

def add_reviewed_keywords(data):
    execute(psql.INSERT_REVIEWED_KEYWORDS, Fetch.EXC, data)

def update_lesson_reviewed_bit(data):
    execute(psql.UPDATE_LESSON_REVIEWED_BIT, Fetch.EXC, data)

def get_keywords_reviewed_bit(data):
    row = execute(psql.GET_KEYWORDS_REVIEWED_BIT, Fetch.ONE, data)
    return row[0]

def get_distinct_levels(data):
    rows = execute(psql.GET_DISTINCT_LEVELS, Fetch.ALL, data)
    levels = [row[0] for row in rows]
    return levels

def get_all_levels():
    rows = execute(psql.GET_ALL_LEVELS, Fetch.ALL)
    levels = [row[0] for row in rows]
    return levels

def get_subject_names(data):
    rows = execute(psql.GET_SUBJECT_NAMES, Fetch.ALL, data)
    subject_names = [row[0] for row in rows]
    return subject_names


def get_all_subject_names(data):
    rows = execute(psql.GET_ALL_SUBJECT_NAMES, Fetch.ALL, data)
    subject_names = [row[0] for row in rows]
    return subject_names    

def get_lesson_names(data):
    rows = execute(psql.GET_LESSON_NAMES, Fetch.ALL, data)
    lesson_names = [row[0] for row in rows]
    return lesson_names
  