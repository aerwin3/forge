"""
The player module holds all the routes
for the player
"""
from flask import Blueprint, render_template, jsonify, request
from forge.models.player import Player
from forge.resources.resource_errors import InvalidRequest
from forge.resources.resources_utils import standardize_json
from forge.models.exceptions import NotFoundException
import logging

players = Blueprint('players', __name__,
                    template_folder='templates')


@players.route('/players', methods=['GET'])
def index():
    players = Player.query.all()
    if request.headers['Accept'] == 'application/json':
        return jsonify(players=[player.serialize for player in players])
    else:
        return render_template('players/index.html', players=players)


@players.route('/players/<id>', methods=['GET'])
def get_player(id):
    try:
        player = Player.get_by_id(id)
        if request.headers['Accept'] == 'application/json':
            return jsonify(player.serialize)
        else:
            return render_template('players/index.html', players=players)
    except NotFoundException as e:
        raise InvalidRequest(e.message, status_code=404)


@players.route('/players', methods=['POST'])
def create():
    if request.headers['Content-Type'] == 'application/json':
        json = request.get_json()       
        try:
            player = Player.create(json)
            return jsonify(player.serialize)
        except Exception as e:
            raise InvalidRequest(e.message, status_code=400)
    return 'your welcome'


@players.route('/players/<id>', methods=['PUT'])
def update(id):
    if request.headers['Content-Type'] == 'application/json':
        json = standardize_json(request.get_json())
        try:
            Player.update(id, json)
            return '', 204
        except NotFoundException as e:
            raise InvalidRequest(e.message, status_code=404)
    return 'your welcome'


@players.route('/players/<id>', methods=['DELETE'])
def delete(id):
    if request.headers['Content-Type'] == 'application/json':
        try:
            Player.delete(id)
            return '', 200
        except NotFoundException as e:
            raise InvalidRequest(e.message, status_code=404)
    return 'your welcome'


