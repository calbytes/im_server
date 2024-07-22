class PSQL_QUERIES:

    GET_AI_KEYWORDS = '''
        SELECT keywords
        FROM ai_keywords
        WHERE keywords_id = %s
    '''
    GET_REVIEWED_KEYWORDS = '''
        SELECT keywords, reviewer
        FROM reviewed_keywords
        WHERE keywords_id = %s
        ORDER BY timestamp DESC
        LIMIT 1;
    '''

    GET_LESSON_CONTENT = '''
        SELECT content_body, lesson_id
        FROM lessons
        WHERE level = %s
        AND subject_name = %s
        AND unit_name = %s
        AND lesson_name = %s
    '''

    INSERT_REVIEWED_KEYWORDS = '''
        INSERT INTO reviewed_keywords
        (keywords_id, keywords, reviewer, timestamp)
        VALUES
        (%s, %s, %s, %s)
    '''

    GET_KEYWORDS_REVIEWED_BIT = '''
        SELECT reviewed
        FROM ai_keywords
        WHERE level = %s
        AND lesson_order = %s
    '''

    GET_DISTINCT_LEVELS = '''
        SELECT DISTINCT level
        FROM lessons
        WHERE reviewed::INTEGER = %s
    '''

    GET_ALL_LEVELS = '''
        SELECT DISTINCT level
        FROM lessons
    '''

    GET_SUBJECT_NAMES = '''
        SELECT DISTINCT subject_name
        FROM lessons
        WHERE reviewed::INTEGER = %s
        AND level = %s
    '''
    GET_ALL_SUBJECT_NAMES = '''
        SELECT DISTINCT subject_name
        FROM lessons
        WHERE level = %s
    '''

    GET_ALL_UNIT_NAMES = '''
        SELECT DISTINCT unit_name
        FROM lessons
        WHERE level = %s
        AND subject_name = %s
    '''

    GET_UNIT_NAMES = '''
        SELECT DISTINCT unit_name
        FROM lessons
        WHERE reviewed::INTEGER = %s
        AND level = %s
        AND subject_name = %s
    '''

    GET_ALL_LESSON_NAMES = '''
        SELECT lesson_name
        from lessons
        WHERE level = %s
        AND subject_name = %s
        AND unit_name = %s
    '''
    GET_LESSON_NAMES = '''
        SELECT lesson_name
        from lessons
        WHERE reviewed::INTEGER = %s
        AND level = %s
        AND subject_name = %s
        AND unit_name = %s
    '''

    UPDATE_LESSON_REVIEWED_BIT = '''
        UPDATE lessons
        SET reviewed = B'1'
        WHERE lesson_id = %s
    '''