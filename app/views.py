from . import app
from flask_cors import cross_origin

@app.route('/')
@cross_origin()
def index():
    return 'Phystech.Genesis Backend API'