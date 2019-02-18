from . import app
from .helpers import json_required, validate_schema
from flask import jsonify, request


@app.route('/')
def index():
    return 'Phystech.Genesis Backend API'

@app.route('/sample_api', methods=['POST'])
@json_required
def sample():
    return jsonify({
        'status': 'OK'
    })
