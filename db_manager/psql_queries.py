class PSQL_QUERIES:

    GET_AI_KEYWORDS = '''
        SELECT keywords
        FROM ai_keywords
        WHERE keywords_id = %s
    '''
    GET_REVIEWED_KEYWORDS = '''
        SELECT keywords, reviewer
        FROM reviewed_keywords
        WHERE lesson_id = %s
        ORDER BY timestamp DESC
        LIMIT 1;
    '''

    GET_LESSON_CONTENT = '''
        SELECT content_body, lesson_id, reviewed
        FROM lessons
        WHERE level = %s
        AND subject_name = %s
        AND unit_name = %s
        AND lesson_name = %s
    '''

    INSERT_REVIEWED_KEYWORDS = '''
        INSERT INTO reviewed_keywords
        (lesson_id, keywords, reviewer, timestamp)
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

    GET_UNREVIEWED_KEYWORD_CONTENT_LEVELS = '''
        SELECT DISTINCT level
        FROM lessons
        WHERE lesson_id IN (
            SELECT DISTINCT lesson_id
            FROM keyword_content
            WHERE approved = 0
        )
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

    GET_UNREVIEWED_KEYWORD_CONTENT_SUBJECT_NAMES = '''
        SELECT DISTINCT subject_name
        FROM lessons
        WHERE level = %s
        AND lesson_id IN (
            SELECT DISTINCT lesson_id
            FROM keyword_content
            WHERE approved = 0
        )
    '''

    GET_ALL_UNIT_NAMES = '''
        SELECT DISTINCT unit_name
        FROM lessons
        WHERE level = %s
        AND subject_name = %s
    '''

    GET_UNIT_NAME = '''
        SELECT unit_name 
        FROM lessons 
        WHERE lesson_name = %s
    '''

    GET_UNIT_NAMES = '''
        SELECT DISTINCT unit_name
        FROM lessons
        WHERE reviewed::INTEGER = %s
        AND level = %s
        AND subject_name = %s
    '''

    GET_UNREVIEWED_KEYWORD_CONTENT_UNIT_NAMES = '''
        SELECT DISTINCT unit_name
        FROM lessons
        WHERE level = %s
        AND subject_name = %s
        AND lesson_id IN (
            SELECT DISTINCT lesson_id
            FROM keyword_content
            WHERE approved = 0
        )
    '''

    GET_ALL_CHAPTER_NAMES = '''
        SELECT DISTINCT chapter_name
        FROM lessons
        WHERE level = %s
        AND subject_name = %s
        AND unit_name = %s
    '''

    GET_CHAPTER_NAMES = '''
        SELECT DISTINCT chapter_name
        FROM lessons
        WHERE reviewed::INTEGER = %s
        AND level = %s
        AND subject_name = %s
        AND unit_name = %s
    '''

    GET_UNREVIEWED_KEYWORD_CONTENT_CHAPTER_NAMES = '''
        SELECT DISTINCT chapter_name
        FROM lessons
        WHERE level = %s
        AND subject_name = %s
        AND unit_name = %s
        AND lesson_id IN (
            SELECT DISTINCT lesson_id
            FROM keyword_content
            WHERE approved = 0
        )
    '''

    GET_ALL_LESSON_NAMES = '''
        SELECT lesson_name
        from lessons
        WHERE level = %s
        AND subject_name = %s
        AND unit_name = %s
        AND chapter_name = %s
    '''
    GET_LESSON_NAMES = '''
        SELECT lesson_name
        from lessons
        WHERE reviewed::INTEGER = %s
        AND level = %s
        AND subject_name = %s
        AND unit_name = %s
        AND chapter_name = %s
    '''
    GET_UNREVIEWED_KEYWORD_CONTENT_LESSON_NAMES = '''
        SELECT DISTINCT lesson_name
        FROM lessons
        WHERE level = %s
        AND subject_name = %s
        AND unit_name = %s
        AND chapter_name = %s
        AND lesson_id IN (
            SELECT DISTINCT lesson_id
            FROM keyword_content
            WHERE approved = 0
        )
    '''

    UPDATE_LESSON_REVIEWED_BIT = '''
        UPDATE lessons
        SET reviewed = B'1'
        WHERE lesson_id = %s
    '''

    UPDATE_KEYWORD_CONTENT = '''
        UPDATE keyword_content
        SET reviewer = %s, approved = %s, timestamp = %s
        WHERE keyword = %s
        AND lesson_id = %s;
    '''

    GET_LEVEL_BY_LESSON_ID = '''
        SELECT level
        FROM lessons
        WHERE lesson_id = %s;
    '''

    GET_KEYWORD_CONTENT = '''
        SELECT content, approved, reviewer
        from keyword_content
        WHERE keyword = %s
        AND lesson_id = %s;
    '''

    GET_KEYWORD_CONTENT_ID = '''
        SELECT keyword_id
        FROM keyword_content
        WHERE keyword = %s
        AND lesson_id = %s
    '''

    INSERT_KEYWORD_CONTENT_DISAPPROVAL_REVIEW = '''
        INSERT INTO keyword_content_reviews
        (keyword_id, keyword, review, reviewer, timestamp)
        VALUES
        (%s, %s, %s, %s, %s)
        ON CONFLICT (keyword_id)
        DO UPDATE SET
            review = EXCLUDED.review,
            reviewer = EXCLUDED.reviewer,
            timestamp = EXCLUDED.timestamp;
    '''

    GET_KEYWORD_CONTENT_REVIEW_BY_ID = '''
        SELECT review
        FROM keyword_content_reviews
        WHERE keyword_id = %s
    '''

    GET_KEYWORD_CONTENT_SET = '''
        SELECT lessons.unit_name, lessons.chapter_name, lessons.lesson_name, keyword_content.keyword, keyword_content.content
        FROM lessons
        INNER JOIN keyword_content ON lessons.lesson_id = keyword_content.lesson_id
        WHERE lessons.level = %s
        AND lessons.subject_name = %s;
    '''

    GET_UPDATED_KEYWORD_CONTENT_SEGMENTS = '''
        SELECT DISTINCT lessons.level, lessons.subject_name
        FROM lessons
        INNER JOIN keyword_content ON lessons.lesson_id = keyword_content.lesson_id
        WHERE keyword_content.timestamp >= NOW() - INTERVAL '7 days';
    '''