"""
This module contains all the routes
for the forge
"""

from forge import app
from flask import jsonify
import players
import resource_errors


app.register_blueprint(players.players)


@app.errorhandler(resource_errors.InvalidRequest)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response



