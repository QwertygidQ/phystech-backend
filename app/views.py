from . import app
from flask import jsonify, request

@app.route('/')
def index():
    return 'Phystech.Genesis Backend API'

@app.route('/sample_api', methods=['POST'])
def sample():
    if request.json:
        return jsonify({
            'status': 'OK'
        })
    
    return jsonify({
        'status': 'Error'
    })