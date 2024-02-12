from flask import jsonify
#from . import api_routes
from flask import Blueprint

api_routes = Blueprint('api', __name__)

@api_routes.route('/greet', methods=['GET'])
def greet():
    data = {'message': 'Welcome to JOE API!'}
    return jsonify(data)

@api_routes.route('/test', methods=['GET'])
def test():
    return "This is a test!!"