from flask import Flask, jsonify, request
import db_manager.db as db
import datetime

app = Flask(__name__)

@app.route('/keywords', methods = ['GET'])
def get_keywords():
    if(request.method == 'GET'):
        try:
            level = request.args.get('level')
            lesson_order = request.args.get("lesson_order")
            data = (level, lesson_order,)
            keywords = []
            reviewed_bit = db.get_keywords_reviewed_bit(data)
            if reviewed_bit == '0':
                keywords = db.get_keywords_by_content_id(data)
            elif reviewed_bit == '1':
                keywords = db.get_reviewed_keywords(data)

            return jsonify(keywords)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        
@app.route('/reviewed_keywords', methods = ['POST'])
def add_reviewed_keywords():
    if(request.method == 'POST'):
        try:
            json = request.get_json()
            level = json.get('level')
            lesson_order = json.get('lesson_order')
            keywords = json.get('keywords')
            reviewer = json.get('reviewer')
            date = datetime.datetime.now()
            data = (level, lesson_order, str(keywords), reviewer, date)
            db.add_reviewed_keywords(data)

            data = (level, lesson_order)
            db.update_ai_keywords_reviewed_bit(data)

            return jsonify({'status': 'success'}), 201
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
