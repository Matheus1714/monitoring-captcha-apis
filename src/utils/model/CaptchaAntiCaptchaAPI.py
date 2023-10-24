from settings import *

from .CaptchaCapSolverAPI import CaptchaCapSolverAPI


class CaptchaAntiCaptchaAPI(CaptchaCapSolverAPI):

    base_url = 'https://api.anti-captcha.com/'
    api_key = API_KEY_ANTI_CAPTCHA