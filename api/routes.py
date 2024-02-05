import os
import traceback

from api import app
from flask import jsonify


@app.route('/test')
def default():
    return "Test"


@app.errorhandler(Exception)
def handle_exception(e):
    error_message = str(e)
    error_message += traceback.format_exc() if \
        os.getenv('FLASK_ENV') == 'development' \
        else ''
    return jsonify(
        error=error_message,
        status=400
    ), 400
