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
            lesson_content = db.get_lesson_content(data)
            dict_obj = lch.get_dict_obj(lesson_content)
            return jsonify(dict_obj)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 

@app.route('/unreviewedKeywordsIDs', methods = ['GET'])
def get_unreviewed_keywords_ids():
    if(request.method == 'GET'):
        try:
            unreviewed_keywords = db.get_unreviewed_keywords_ids()
            return jsonify(unreviewed_keywords)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 

@app.route('/reviewedKeywordsIDs', methods = ['GET'])
def get_reviewed_keywords_ids():
    if(request.method == 'GET'):
        try:
            reviewed_keywords = db.get_reviewed_keywords_ids()
            return jsonify(reviewed_keywords)
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
            print(str(type(subject_names)))
            print(subject_names)
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
            print(str(type(lesson_names)))
            print(lesson_names)
            return jsonify(lesson_names)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        