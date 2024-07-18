from flask import Flask, jsonify, request
import db_manager.db as db
import datetime
import json
from utils import lesson_content_handler as lch

app = Flask(__name__)

@app.route('/keywords', methods = ['GET'])
def get_keywords():
    if(request.method == 'GET'):
        try:

            print("TODO")
            raise Exception("changed table structure")

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        
@app.route('/reviewed_keywords', methods = ['POST'])
def add_reviewed_keywords():
    if(request.method == 'POST'):
        try:
            json = request.get_json()
            keywords_id = json.get('keywords_id')
            keywords = json.get('keywords')
            reviewer = json.get('reviewer')
            date = datetime.datetime.now()
            data = (keywords_id, str(keywords), reviewer, date)
            print(data)
            db.add_reviewed_keywords(data)

            data = (keywords_id,)
            db.update_lesson_reviewed_bit(data)

            return jsonify({'status': 'success'}), 201
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        
@app.route('/lesson_and_keywords', methods = ['GET'])
def get_lesson_content_and_keywords():
    if(request.method == 'GET'):
        try:
            reviewed = request.args.get('reviewed')
            level = request.args.get('level')
            subject_name = request.args.get('subject_name')
            lesson_name = request.args.get('lesson_name')
            data = (reviewed, level, subject_name, lesson_name)
            row = db.get_lesson_content(data)
            lesson_content = row[0]
            lesson_id = row[1]

            data = (lesson_id,)
            keywords = []
            print(str(type(reviewed)))
            if reviewed == '1':
                print("getting rev kw")
                keywords = db.get_reviewed_keywords(data)
            else:
                print("getting ai kw")
                keywords = db.get_ai_keywords(data)

            response = {
                'lesson': lesson_content,
                'keywords': keywords,
                'lesson_id': lesson_id
            }

            return jsonify(response)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        
@app.route('/distinct_levels', methods = ['GET'])
def get_distinct_levels():
    if(request.method == 'GET'):
        try:
            reviewed = request.args.get('reviewed')
            data = (reviewed,)
            levels = db.get_distinct_levels(data)
            return jsonify(levels)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        
@app.route('/subject_names', methods = ['GET'])
def get_subject_names():
    if(request.method == 'GET'):
        try:
            reviewed = request.args.get('reviewed')
            level = request.args.get('level')
            data = (reviewed, level)
            subject_names = db.get_subject_names(data)
            return jsonify(subject_names)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        

@app.route('/lesson_names', methods = ['GET'])
def get_lesson_names():
    if(request.method == 'GET'):
        try:
            reviewed = request.args.get('reviewed')
            level = request.args.get('level')
            subject_name = request.args.get('subject_name')
            data = (reviewed, level, subject_name)
            lesson_names = db.get_lesson_names(data)
            return jsonify(lesson_names)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        