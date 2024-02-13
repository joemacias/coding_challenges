from flask import jsonify
from app.config import Config
from flask import Blueprint

"""
This script defines different endpoints in the app
"""

api_routes = Blueprint('api', __name__)

# Rate limit middleware
@api_routes.before_request
def check_rate_limit():
    from middleware.rate_limit import rate_limit_f
    return rate_limit_f(Config)

# Endpoint return data in JSON format
@api_routes.route('/data', methods=['GET'])
def data():
    data = {'message': 'Welcome to JOE API!'}
    return jsonify(data)
# Endpoint return test message
@api_routes.route('/test', methods=['GET'])
def test():
    return "This is a test!!"
# Endpoint validated rate limitation module
@api_routes.route('/unlimited', methods=['GET'])
def unlimited():
    return "Unlimited! Let's Go!"
# Endpoint validated rate limitation module
@api_routes.route('/limited', methods=['GET'])
def limited():
    return "Limited, don't over use me!"