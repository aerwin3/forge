"""
The player module holds all the routes
for the player
"""
from flask import Blueprint, render_template, jsonify, request
from forge.models.player import Player
from forge.resources.resource_errors import InvalidRequest


players = Blueprint('players', __name__,
                    template_folder='templates')


@players.route('/players', methods=['GET'])
def index():
    players = Player.query.all()
    if request.headers['Accept'] == 'application/json':
        return jsonify(players=[player.serialize for player in players])
    else:
        return render_template('players/index.html', players=players)


@players.route('/players', methods=['POST'])
def create():
    if request.headers['Content-Type'] == 'application/json':
        json = request.get_json()
        for key, value in json.iteritems():
            json[key] = str(value)
        try:
            player = Player.create_player(json)
            return jsonify(player.serialize)
        except Exception as e:
            raise InvalidRequest(e.message, status_code=400)
    return 'your welcome'


@players.route('/players/new')
def new():
    return render_template('players/new.html')
