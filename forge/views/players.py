"""
The player module holds all the routes
for the player
"""
from flask import Blueprint, render_template, jsonify, request
from forge.models.player import Player

players = Blueprint('players', __name__,
                    template_folder='templates')


@players.route('/players')
def index():
    players = Player.query.all()
    if request.headers['Accept'] == 'application/json':
        return jsonify(players=[player.serialize for player in players])
    else:
        return render_template('players/index.html', players=players)


@players.route('/players/new')
def new():
    return render_template('players/new.html')

