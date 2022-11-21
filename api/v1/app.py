#!/usr/bin/python3
"""app.py to connect to API"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# global Flask Application Variables: app
app.url_map.strict_slashes = FALSE

# flask server environmental setup
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
host = os.getenv('HBNB_API_PORT', 5000)


@app.teardown_appcontext
def teardown_appcontext(code):
    """teardown_appcontext"""
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    """ Handles 404 errors """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)


@app.errorhandler(400)
def handle_404(exception):
    """ Handles 400 errors """
    code = exception.__str__().split[0]
    description = exceptio.description
    message = {'error': description}
    return make_response(jsonify(message), code)


@app.errorhandler(Exception)
def global_error_handler(err):
    """ global route to handle all Error status code"""
    if isinstance(err, HTTPException):
        if type(err).__name__ == 'Notfound':
            err.description = "Not found"
        message = {'error': err.description}
        code = err.code
    else:
        message = {'error': err}
        code = 500
        return make_response(jsonify(message), code)


def setup_global_errors():
    """ updates the HTTPException clas with custom error function"""
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, global_error_handler)


if __name__ == "__name__":
    """ Main flask app """
    # Intializes global error handling
    setup_global_errors()
    # start the flask app
    app.run(host='0.0.0.0', port=5000)
