from flask import Flask, jsonify, request
import db_manager.db as db

import db_manager.db as db

app = Flask(__name__)

@app.route('/keywords', methods = ['GET'])
def get_keywords():
    if(request.method == 'GET'):
        try:
            id = request.args.get('id')
            data = (id,)
            keywords = db.get_keywords_by_content_id(data)
            return jsonify(keywords)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        
@app.route('/lesson', methods = ['GET'])
def get_lesson_content():
    if(request.method == 'GET'):
        try:
            level = request.args.get('level')
            lesson_order = request.args.get('lesson_order')
            data = (level, lesson_order,)
            lesson_content = db.get_content(data)
            return jsonify(lesson_content)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 

        
@app.route('/getUnreviewedKeywordsIDs', methods = ['GET'])
def get_unreviewed_keywords_ids():
    if(request.method == 'GET'):
        try:
            unreviewed_keywords = db.get_unreviewed_keywords_ids()
            return jsonify(unreviewed_keywords)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 

@app.route('/test', methods = ['GET'])
def get_test():
    if(request.method == 'GET'):
        try:
            level = request.args.get('level')
            lesson_order = request.args.get('lesson_order')
            print(str(level) + str(lesson_order))

            data = [('Grade 6', '1'), ('Grade 6', '3')]
            return jsonify(data)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
