from flask import Blueprint, jsonify
import http

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def root():
    return jsonify({
        'error': 0,
        'status': http.HTTPStatus.OK,
        'message': 'Welcome to my API'
    })