from src.utils.model.ResponseDTOModel import ResponseDTOModel

from flask import Blueprint, jsonify
import http

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def root():
    response_dto = ResponseDTOModel(message='Welcome to my api!')
    response = jsonify(response_dto.get_response())
    status = http.HTTPStatus.OK
    return response, status