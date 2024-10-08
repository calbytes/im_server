from flask import Flask, jsonify, request
import db_manager.db as db
import datetime
import json

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
        
@app.route('/distinct_levels', methods = ['GET'])
def get_distinct_levels():
    if(request.method == 'GET'):
        try:
            reviewed = request.args.get('reviewed')
            levels = []
            if(reviewed == '2'):
                levels = db.get_all_levels()
            elif(reviewed == '3'):
                levels = db.get_unreviewed_keyword_content_levels()
            else:
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

            subject_names = []
            if(reviewed == '2'):
                data = (level,)
                subject_names = db.get_all_subject_names(data)
            elif(reviewed == '3'):
                data = (level,)
                subject_names = db.get_unreviewed_keyword_content_subject_names(data)
            else:
                data = (reviewed, level)
                subject_names = db.get_subject_names(data)

            return jsonify(subject_names)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        
@app.route('/unit_names', methods = ['GET'])
def get_unit_names():
    if(request.method == 'GET'):
        try:
            reviewed = request.args.get('reviewed')
            level = request.args.get('level')
            subject_name = request.args.get('subject_name')

            unit_names = []
            if(reviewed == '2'):
                data = (level, subject_name)
                unit_names = db.get_all_unit_names(data)
            elif(reviewed == '3'):
                data = (level, subject_name)
                unit_names = db.get_unreviewed_keyword_content_unit_names(data)
            else:
                data = (reviewed, level, subject_name)
                unit_names = db.get_unit_names(data)

            return jsonify(unit_names)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        
@app.route('/chapter_names', methods = ['GET'])
def get_chapter_names():
    if(request.method == 'GET'):
        try:
            reviewed = request.args.get('reviewed')
            level = request.args.get('level')
            subject_name = request.args.get('subject_name')
            unit_name = request.args.get('unit_name')

            chapter_names = []
            if(reviewed == '2'):
                data = (level, subject_name, unit_name)
                chapter_names = db.get_all_chapter_names(data)
            elif(reviewed == '3'):
                data = (level, subject_name, unit_name)
                chapter_names = db.get_unreviewed_keyword_content_chapter_names(data)
            else:
                data = (reviewed, level, subject_name, unit_name)
                chapter_names = db.get_chapter_names(data)

            return jsonify(chapter_names)
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
            unit_name = request.args.get('unit_name')
            chapter_name = request.args.get('chapter_name')

            lesson_names = []
            if(reviewed == '2'):
                data = (level, subject_name, unit_name, chapter_name)
                lesson_names = db.get_all_lesson_names(data)
            elif(reviewed == '3'):
                data = (level, subject_name, unit_name, chapter_name)
                lesson_names = db.get_unreviewed_keyword_content_lesson_names(data)
            else:
                data = (reviewed, level, subject_name, unit_name, chapter_name)
                lesson_names = db.get_lesson_names(data)
            
            return jsonify(lesson_names)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 

@app.route('/lesson_and_keywords', methods = ['GET'])
def get_lesson_content_and_keywords():
    if(request.method == 'GET'):
        try:
            level = request.args.get('level')
            subject_name = request.args.get('subject_name')
            unit_name = request.args.get('unit_name')
            lesson_name = request.args.get('lesson_name')

            data = (level, subject_name, unit_name, lesson_name)
            row = db.get_lesson_content(data)
            lesson_content = row[0]
            lesson_id = row[1]
            is_reviewed = row[2]

            data = (lesson_id,)
            last_reviewed_by = ''
            keywords = []
            if is_reviewed == '0':
                keywords = db.get_ai_keywords(data)
            elif is_reviewed == '1':
                row = db.get_reviewed_keywords(data)
                keywords = row[0]
                last_reviewed_by = row[1]

            response = {
                'lesson': lesson_content,
                'keywords': keywords,
                'lesson_id': lesson_id,
                'last_reviewed_by': last_reviewed_by
            }

            return jsonify(response)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404

@app.route('/reviewed_keywords', methods = ['POST'])
def add_reviewed_keywords():
    if(request.method == 'POST'):
        try:
            json = request.get_json()
            lesson_id = json.get('lesson_id')
            keywords = json.get('keywords')
            reviewer = json.get('reviewer')
            date = datetime.datetime.now()
            data = (lesson_id, str(keywords), reviewer, date)
            db.add_reviewed_keywords(data)

            data = (lesson_id,)
            db.update_lesson_reviewed_bit(data)

            return jsonify({'status': 'success'}), 201
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
       
@app.route('/keyword_content', methods = ['GET', 'POST'])
def update_keyword_content():
    if(request.method == 'GET'):
        try:
            keyword = request.args.get('keyword').strip()
            lesson_id = request.args.get('lesson_id')
            data = (keyword, lesson_id)
            res = db.get_keyword_content(data)

            keyword_content = res[0]
            approved = res[1]
            reviewer = ''
            disapproval_review = ''
            
            if approved == -1 :
                data = (keyword, lesson_id)
                keyword_id = db.get_keyword_content_id(data)
                data = (keyword_id,)
                disapproval_review = db.get_keyword_content_review_by_id(data)
            if approved != 0 :
                reviewer = res[2]

            response = {
                'keyword_content': keyword_content,
                'reviewer': reviewer,
                'disapproval_review': disapproval_review,
                'approval': str(approved)
            }
            
            return jsonify(response)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404
        
    if(request.method == 'POST'):
        try:
            json = request.get_json()
            approved = json.get('approved')
            keyword = json.get('keyword').strip()
            lesson_id = json.get('lesson_id')
            notes = json.get('notes')
            reviewer = json.get('reviewer')
            date = datetime.datetime.now()

            data = (reviewer, approved, date, keyword, lesson_id)
            db.update_keyword_content(data)

            data = (keyword, lesson_id)
            keyword_id = db.get_keyword_content_id(data)

            if approved == -1:
                data = (keyword_id, keyword, notes, reviewer, date)
                db.insert_keyword_content_disapproval_review(data)

            return jsonify({'status': 'success'}), 201
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404 
        
@app.route('/keyword_content_set', methods = ['GET'])
def get_keyword_content_set():
    if(request.method == 'GET'):
        try:
            level = request.args.get('level')
            subject_name = request.args.get('subject_name')

            data = (level, subject_name)
            rows = db.get_keyword_content_set(data)

            cols = ['unit_name', 'chapter_name', 'lesson_name', 'keyword', 'keyword_content']
            set = [dict(zip(cols, row)) for row in rows]

            return jsonify(set)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404
        
@app.route('/updated_segments', methods = ['GET'])
def get_udpated_segments():
    if(request.method == 'GET'):
        try:
            rows = db.get_updated_segments()
            cols = ['level', 'subject']
            segments = [dict(zip(cols, row)) for row in rows]
            return jsonify(segments)
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 
                            'message': 'There was an error processing the request'}), 404