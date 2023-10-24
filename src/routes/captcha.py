import http

from flask import Blueprint, jsonify
from typing import Tuple

from src.utils.model.BaseCaptchaResponseModel import BaseCaptchaResponseModel
from src.utils.model.CaptchaAntiCaptchaAPI import CaptchaAntiCaptchaAPI
from src.utils.model.CaptchaCapSolverAPI import CaptchaCapSolverAPI
from src.utils.model.CaptchaTwoCaptchaAPI import CaptchaTwoCaptchaAPI
from src.utils.model.ResponseCaptchaDTOModel import ResponseCaptchaDTOModel
from src.utils.model.ResponseDataDTOModel import ResponseDataDTOModel

captcha = Blueprint('captcha', __name__)

def get_balance_response(api: BaseCaptchaResponseModel, message: str)->Tuple[dict, http.HTTPStatus]:
    balance = api.get_balance()
    response_dto = ResponseCaptchaDTOModel(balance=balance, message=message)

    response_dict = response_dto.get_response()
    status = http.HTTPStatus.OK

    return response_dict, status

@captcha.route('/balance', methods=['GET'])
def get_all_balance():
    apis = [
        (CaptchaAntiCaptchaAPI(), 'Anticaptcha balance'),
        (CaptchaTwoCaptchaAPI(), 'TwoCaptcha balance'),
        (CaptchaCapSolverAPI(), 'CapSolver balance')
    ]
    data = []

    status = http.HTTPStatus.OK
    for api, message in apis:
        response_dict, status = get_balance_response(api, message)
        data.append(response_dict)

    response_dto = ResponseDataDTOModel(data=data)

    return jsonify(response_dto.get_response()), status

@captcha.route('/balance/anti-captcha', methods=['GET'])
def balance_anti_captcha():
    api = CaptchaAntiCaptchaAPI()
    response_dict, status = get_balance_response(api, 'Anticaptcha balance')
    return jsonify(response_dict), status

@captcha.route('/balance/two-captcha', methods=['GET'])
def balance_two_captcha():
    api = CaptchaTwoCaptchaAPI()
    response_dict, status = get_balance_response(api, 'TwoCaptcha balance')
    return jsonify(response_dict), status

@captcha.route('/balance/cap-solver', methods=['GET'])
def balance_cap_solver():
    api = CaptchaCapSolverAPI()
    response_dict, status = get_balance_response(api, 'CapSolver balance')
    return jsonify(response_dict), status