import db_manager.db as db

def test_db():
    id = 1
    data = (id,)
    keywords = db.get_keywords_by_content_id(data)
    print(str(keywords))


if __name__ == '__main__':
    test_db()