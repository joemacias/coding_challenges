from flask import Flask
from app.config import Config

"""
This script define app structure and behaviour
"""

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = Config.SECRET_KEY

# Import endpoints blueprints
from app.routes import api_routes
# Import Initiation method in rate limit module
from middleware.rate_limit import initialize_rate_limit_values

# Flag to ensure initialization occurs only once
initialized = False
@app.before_request
def before_first_request():
    global initialized
    # Check if initialization has occurred
    if not initialized:
        initialize_rate_limit_values(Config)
        initialized = True

# Register endpoints blueprints
app.register_blueprint(api_routes.api_routes, url_prefix='/api')