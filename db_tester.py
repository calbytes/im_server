import db_manager.db as db
import datetime
import json
from utils import lesson_content_handler as lch

def test_db():
    id = 1
    data = (id,)
    keywords = db.get_keywords_by_content_id(data)
    print(str(keywords))

def get_unreviewed_keywords():
    rows = db.get_unreviewed_keywords_ids()
    print(rows)

def get_reviewed_keywords_ids():
    rows = db.get_reviewed_keywords_ids()
    print(rows)

def get_lesson_content():
    level = 'Grade 6'
    lesson_order = 4
    data = (level, lesson_order,)
    lesson_content = db.get_lesson_content(data)
    dict_obj = lch.get_dict_obj(lesson_content)
    print("dict_obj type: " + str(type(dict_obj)))
    print(dict_obj)

def date():
    date = datetime.datetime.now()
    print(date)

def get_keywords():
    data = ('Grade 6', '5')
    response = db.get_keywords_reviewed_bit(data)
    print(type(response[0]))

def get_levels():
    reviewed = '0'
    data = (reviewed,)
    levels = db.get_distinct_levels(data)
    print(levels) 


if __name__ == '__main__':
    get_levels()