"""
This module contains all the routes
for the forge
"""

from forge import app
import players

app.register_blueprint(players.players)



