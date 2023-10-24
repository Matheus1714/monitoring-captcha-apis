from urllib.parse import urljoin

from settings import *

from .CaptchaResponseModel import CaptchaResponseModel


class CaptchaCapSolverAPI(CaptchaResponseModel):

    base_url = 'https://api.capsolver.com/'
    api_key = API_KEY_CAP_SOLVER

    def get_balance(self)->float:
        url = urljoin(self.base_url, '/getBalance')
        body = {
            "clientKey": self.api_key
        }

        data = self.send_request(url, body)
        is_response_error =  data.get('errorId') == 1

        if not data or is_response_error:
            return 0.0
        
        balance = float(data.get('balance', 0))

        return balance

    def has_balance(self)->bool:
        balance = self.get_balance()
        return not not balance