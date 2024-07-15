import db_manager.db as db
import datetime

def test_db():
    id = 1
    data = (id,)
    keywords = db.get_keywords_by_content_id(data)
    print(str(keywords))

def get_unreviewed_keywords():
    rows = db.get_unreviewed_keywords_ids()
    print(rows)

def get_lesson_content():
    level = 'Grade 6'
    lesson_order = 4
    data = (level, lesson_order,)
    row = db.get_content(data)
    print(row)

def date():
    date = datetime.datetime.now()
    print(date)

def get_keywords():
    data = ('Grade 6', '5')
    response = db.get_keywords_reviewed_bit(data)
    print(type(response[0]))


if __name__ == '__main__':
    get_keywords()