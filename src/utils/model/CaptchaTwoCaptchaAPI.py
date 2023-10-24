import requests

from settings import *

from .CaptchaCapSolverAPI import CaptchaCapSolverAPI


class CaptchaTwoCaptchaAPI(CaptchaCapSolverAPI):

    base_url = 'http://2captcha.com/'
    api_key = API_KEY_TWO_CAPCHA

    def send_request(self, url:str, params:dict = {})->dict:
        try:
            response = requests.post(url)
            if response.text.startswith("ERROR"):
                return 0.0

            balance = float(response.text)
            return {
                'balance': balance
            }
        except Exception as e:
            return {}

    def get_balance(self)->float:
        url = f"{self.base_url}res.php?key={self.api_key}&action=getbalance"

        data = self.send_request(url)
        
        balance = float(data.get('balance', 0))

        return balance