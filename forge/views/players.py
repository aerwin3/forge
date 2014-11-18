"""
The player module holds all the routes
for the player
"""
from flask import Blueprint, render_template

players = Blueprint('players', __name__,
                    template_folder='templates')


@players.route('/players')
def index():
    return render_template('players/index.html')