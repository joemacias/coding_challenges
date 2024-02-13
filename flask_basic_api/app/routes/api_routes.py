from flask import jsonify
#from . import api_routes
from flask import Blueprint

api_routes = Blueprint('api', __name__)

@api_routes.route('/data', methods=['GET'])
def data():
    data = {'message': 'Welcome to JOE API!'}
    return jsonify(data)

@api_routes.route('/test', methods=['GET'])
def test():
    return "This is a test!!"

@api_routes.route('/unlimited', methods=['GET'])
def unlimited():
    return "Unlimited! Let's Go!"

@api_routes.route('/limited', methods=['GET'])
def limited():
    return "Limited, don't over use me!"