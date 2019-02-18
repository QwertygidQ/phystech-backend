from flask import request, jsonify
from functools import wraps
from schema import SchemaError


def json_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not request.data or not request.json:
            return jsonify({
                'status': 'Error',
                'reason': 'No JSON provided'
            })
        return func(*args, **kwargs)

    return wrapper

def validate_schema(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                schema.validate(request.json)
            except SchemaError:
                return jsonify({
                    'status': 'Error',
                    'reason': 'Invalid JSON provided'
                })
            
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator