from flask import request, jsonify, session
import time


"""
These methods implement rate limit request in a particular endpoint
"""

def initialize_rate_limit_values(config) -> None:
    # Define the time and tokens reference in a session
    session['last_request_time'] = time.time()
    session['tokens'] = config.BUCKET_CAPACITY

def rate_limit_f(config):
    
    # Define the endpoint to be rate_limited
    if request.endpoint == config.RATE_LIMIT_ENDPOINT:
        # Calculate the gab between the last request
        current_time = time.time()
        elapsed_time = current_time - session['last_request_time']

        # Refill the token bucket based on the elapsed time
        session['tokens'] = min(session['tokens'] + elapsed_time*config.TOKEN_RATE, config.BUCKET_CAPACITY)

        # Update the last request time
        session['last_request_time'] = current_time

        # Check if there are tokens availables
        if session['tokens'] >= 1:
            print("tokens good")
            # Remove a token
            session['tokens'] -= 1
        else:
            print("tokens out")
            # Return error message for rate limit
            return jsonify({'error': 'Rate limit exceeded'}), 429

