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
    return row

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

def get_unreviewed_keyword_content_levels():
    rows = execute(psql.GET_UNREVIEWED_KEYWORD_CONTENT_LEVELS, Fetch.ALL)
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

def get_unreviewed_keyword_content_subject_names(data):
    rows = execute(psql.GET_UNREVIEWED_KEYWORD_CONTENT_SUBJECT_NAMES, Fetch.ALL, data)
    subject_names = [row[0] for row in rows]
    return subject_names

def get_all_unit_names(data):
    rows = execute(psql.GET_ALL_UNIT_NAMES, Fetch.ALL, data)
    unit_names = [row[0] for row in rows]
    return unit_names 

def get_unit_name(data):
    row = execute(psql.GET_UNIT_NAME, Fetch.ONE, data)
    return row

def get_unit_names(data):
    rows = execute(psql.GET_UNIT_NAMES, Fetch.ALL, data)
    unit_names = [row[0] for row in rows]
    return unit_names

def get_unreviewed_keyword_content_unit_names(data):
    rows = execute(psql.GET_UNREVIEWED_KEYWORD_CONTENT_UNIT_NAMES, Fetch.ALL, data)
    unit_names = [row[0] for row in rows]
    return unit_names

def get_all_chapter_names(data):
    rows = execute(psql.GET_ALL_CHAPTER_NAMES, Fetch.ALL, data)
    chapter_names = [row[0] for row in rows]
    return chapter_names 

def get_chapter_names(data):
    rows = execute(psql.GET_CHAPTER_NAMES, Fetch.ALL, data)
    chapter_names = [row[0] for row in rows]
    return chapter_names

def get_unreviewed_keyword_content_chapter_names(data):
    rows = execute(psql.GET_UNREVIEWED_KEYWORD_CONTENT_CHAPTER_NAMES, Fetch.ALL, data)
    chapter_names = [row[0] for row in rows]
    return chapter_names

def get_all_lesson_names(data):
    rows = execute(psql.GET_ALL_LESSON_NAMES, Fetch.ALL, data)
    lesson_names = [row[0] for row in rows]
    return lesson_names    

def get_lesson_names(data):
    rows = execute(psql.GET_LESSON_NAMES, Fetch.ALL, data)
    lesson_names = [row[0] for row in rows]
    return lesson_names

def get_unreviewed_keyword_content_lesson_names(data):
    rows = execute(psql.GET_UNREVIEWED_KEYWORD_CONTENT_LESSON_NAMES, Fetch.ALL, data)
    lesson_names = [row[0] for row in rows]
    return lesson_names
  
def update_keyword_content(data):
    execute(psql.UPDATE_KEYWORD_CONTENT, Fetch.EXC, data)

def get_level_by_lesson_id(data):
    row = execute(psql.GET_LEVEL_BY_LESSON_ID, Fetch.ONE, data)
    return row[0]

def get_keyword_content(data):
    row = execute(psql.GET_KEYWORD_CONTENT, Fetch.ONE, data)
    return row

def get_keyword_content_id(data):
    row = execute(psql.GET_KEYWORD_CONTENT_ID, Fetch.ONE, data)
    return row[0]

def insert_keyword_content_disapproval_review(data):
    execute(psql.INSERT_KEYWORD_CONTENT_DISAPPROVAL_REVIEW, Fetch.EXC, data)

def get_keyword_content_review_by_id(data):
    row = execute(psql.GET_KEYWORD_CONTENT_REVIEW_BY_ID, Fetch.ONE, data)
    return row[0]

def get_keyword_content_set(data):
    rows = execute(psql.GET_KEYWORD_CONTENT_SET, Fetch.ALL, data)
    return rows 

def get_updated_segments():
    rows = execute(psql.GET_UPDATED_KEYWORD_CONTENT_SEGMENTS, Fetch.ALL)
    return rows