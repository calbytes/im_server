import db_manager.db as db
import datetime
import json
from utils import lesson_content_handler as lch

def get_lesson_content():
    reviewed = '0'
    level = 'Grade 6'
    subject_name = 'Mathematics'
    lesson_name = 'Understand the term: product'
    data = (reviewed, level, subject_name, lesson_name)
    lesson_content = db.get_lesson_content(data)
    #dict_obj = lch.get_dict_obj(lesson_content)
    print("lesson_content type: " + str(type(lesson_content)))
    print(lesson_content)

def date():
    date = datetime.datetime.now()
    print(date)

def get_keywords():
    data = (6,)
    response = db.get_ai_keywords(data)
    print(response)
    print(type(response[0]))

def get_levels():
    reviewed = '1'
    data = (reviewed,)
    levels = db.get_distinct_levels(data)
    print(levels) 

def get_subject_names():
    reviewed = '0'
    level = 'Grade 6'
    data = (reviewed, level)
    subject_names = db.get_subject_names(data)
    print(subject_names)

def get_lesson_names():
    reviewed = '0'
    level = 'Grade 999'
    subject_name = 'Test Subject'
    data = (reviewed, level, subject_name)
    subject_names = db.get_lesson_names(data)
    print(len(subject_names))

def compare_str_lens():
    un = 'Spatial Reasoning'
    print(len(un))
    data = ('Naming lines',)
    res = db.get_unit_name(data)[0]
    print(len(res))

if __name__ == '__main__':
    compare_str_lens()