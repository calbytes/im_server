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
    GET_REVIEWED_KEYWORDS_IDS = '''
        SELECT level, lesson_order
        FROM ai_keywords
        where reviewed::INTEGER = 1
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

    GET_KEYWORDS_REVIEWED_BIT = '''
        SELECT reviewed
        FROM ai_keywords
        WHERE level = %s
        AND lesson_order = %s
    '''

    GET_REVIEWED_KEYWORDS = '''
        SELECT keywords
        FROM reviewed_keywords
        WHERE level = %s
        AND lesson_order = %s
    '''

    UPDATE_AI_KEYWORDS_REVIEWED_BIT = '''
        UPDATE ai_keywords
        SET reviewed = B'1'
        WHERE level = %s 
        AND lesson_order = %s
    '''

    GET_DISTINCT_LEVELS = '''
        SELECT DISTINCT level
        FROM lessons
        WHERE reviewed::INTEGER = %s
    '''

    GET_SUBJECT_NAMES = '''
        SELECT DISTINCT subject_name
        FROM lessons
        WHERE reviewed::INTEGER = %s
        AND level = %s
    '''

    GET_LESSON_NAMES = '''
        SELECT lesson_name
        from lessons
        WHERE reviewed::INTEGER = %s
        AND level = %s
        AND subject_name = %s
    '''