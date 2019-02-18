from . import app

@app.route('/')
def index():
    return 'Phystech.Genesis Backend API'