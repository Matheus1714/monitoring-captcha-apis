import http

from flask import Blueprint, jsonify

from src.utils.model.BaseCaptchaResponseModel import BaseCaptchaResponseModel
from src.utils.model.CaptchaAntiCaptchaAPI import CaptchaAntiCaptchaAPI
from src.utils.model.CaptchaCapSolverAPI import CaptchaCapSolverAPI
from src.utils.model.CaptchaTwoCaptchaAPI import CaptchaTwoCaptchaAPI
from src.utils.model.ResponseCaptchaDTOModel import ResponseCaptchaDTOModel
from src.utils.model.ResponseDataDTOModel import ResponseDataDTOModel

captcha = Blueprint('captcha', __name__)

@captcha.route('/balance', methods=['GET'])
def get_all_balance():
    apis = [CaptchaAntiCaptchaAPI(), CaptchaTwoCaptchaAPI(), CaptchaCapSolverAPI()]
    data = []

    for api in apis:
        api:BaseCaptchaResponseModel
        balance = api.get_balance()

        response_dto = ResponseCaptchaDTOModel(balance = balance, message='')
        data.append(response_dto.get_response())

    response_dto = ResponseDataDTOModel(data = data)

    response = jsonify(response_dto.get_response())
    status = http.HTTPStatus.OK

    return response, status

@captcha.route('/balance/anti-captcha', methods=['GET'])
def balance_anti_captcha():
    api = CaptchaAntiCaptchaAPI()
    balance = api.get_balance()

    response_dto = ResponseCaptchaDTOModel(balance = balance, message='Anticaptcha balance')
    response = jsonify(response_dto.get_response())
    status = http.HTTPStatus.OK

    return response, status

@captcha.route('/balance/two-captcha', methods=['GET'])
def balance_two_captcha():
    api = CaptchaTwoCaptchaAPI()
    balance = api.get_balance()

    response_dto = ResponseCaptchaDTOModel(balance = balance, message='TwoCaptcha balance')
    response = jsonify(response_dto.get_response())
    status = http.HTTPStatus.OK

    return response, status

@captcha.route('/balance/cap-solver', methods=['GET'])
def balance_cap_solver():
    api = CaptchaCapSolverAPI()
    balance = api.get_balance()

    response_dto = ResponseCaptchaDTOModel(balance = balance, message='CapSolver balance')
    response = jsonify(response_dto.get_response())
    status = http.HTTPStatus.OK

    return response, status