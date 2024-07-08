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
            return jsonify({'status': 'error', 'message': 'There was an error processing the request'}), 404 
        
@app.route('/getUnreviewedKeywordsIDs', methods = ['GET'])
def get_next_keywords_review():
    if(request.method == 'GET'):
        try:
            unreviewed_keywords = db.get_unreviewed_keywords_ids()
            key = ['unreviewed']
            response = dict(zip(key, unreviewed_keywords))
            return jsonify(response)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 'message': 'There was an error processing the request'}), 404 

