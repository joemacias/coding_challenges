from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.routes import api_routes

app.register_blueprint(api_routes.api_routes, url_prefix='/api')

