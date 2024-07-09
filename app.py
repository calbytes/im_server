from flask import Flask, jsonify, request
import db_manager.db as db

import db_manager.db as db

app = Flask(__name__)

@app.route('/keywords', methods = ['POST'])
def get_keywords():
    if(request.method == 'POST'):
        try:
            json_data = request.get_json()
            id = json_data.get('id')
            data = (id,)
            keywords = db.get_keywords_by_content_id(data)
            keys = ['keywords']
            response = dict(zip(keys, keywords))
            return jsonify(response)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        
@app.route('/getContent', methods = ['POST'])
def getContent():
    if(request.method == 'POST'):
        try:
            json_data = request.get_json()
            level = json_data.get('level')
            lesson_order = json_data.get('lesson_order')
            data = (level, lesson_order,)
            lesson_content = db.get_content(data)
            return jsonify(lesson_content)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 

        
@app.route('/getUnreviewedKeywordsIDs', methods = ['GET'])
def get_next_keywords_review():
    if(request.method == 'GET'):
        try:
            unreviewed_keywords = db.get_unreviewed_keywords_ids()
            return jsonify(unreviewed_keywords)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 

