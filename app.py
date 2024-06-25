'''
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/getContentKeywords', methods = ['POST'])
def get_content_keywords():
    if(request.method == 'POST'):
        try:

            return jsonify({'status': 'success'}), 201
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 'message': 'There was an error processing the request'}), 500 

@app.route('/getKeywordsByContent', methods = ['POST'])
def get_content_keywords():
    if(request.method == 'POST'):
        try:

            return jsonify({'status': 'success'}), 201
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            return jsonify({'status': 'error', 'message': 'There was an error processing the request'}), 500 


if __name__ == '__main__':
    app.run(host='0.0.0.0')
'''