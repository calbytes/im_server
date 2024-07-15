class PSQL_QUERIES:

    GET_KEYWORDS_BY_ID = '''
        SELECT keywords
        FROM ai_keywords
        WHERE level = %s
        AND lesson_order = %s
    '''

    GET_UNREVIEWED_KEYWORDS_IDS = '''
        SELECT level, lesson_order
        FROM ai_keywords
        where reviewed::INTEGER = 0
    '''

    GET_LESSON_CONTENT = '''
        SELECT data
        FROM lesson
        WHERE level = %s
        AND lesson_order = %s
    '''

    INSERT_REVIEWED_KEYWORDS = '''
        INSERT INTO reviewed_keywords
        (level, lesson_order, keywords, reviewer, date)
        VALUES
        (%s, %s, %s, %s, %s)
    '''