class PSQL_QUERIES:

    # Icon Math Queries
    GET_KEYWORDS_BY_ID = '''
        SELECT keywords
        FROM keywords
        WHERE lesson_order = %s
    '''
