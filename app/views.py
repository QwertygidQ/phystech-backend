from . import app
from flask_cors import cross_origin
from flask import jsonify, request

@app.route('/')
@cross_origin()
def index():
    return 'Phystech.Genesis Backend API'

@app.route('/sample_api', methods=['POST'])
@cross_origin()
def sample():
    if request.json:
        return jsonify({
            'status': 'OK'
        })
    
    return jsonify({
        'status': 'Error'
    })