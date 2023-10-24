from .BaseResponseModel import BaseResponseModel

import requests

class ResponseModel(BaseResponseModel):

    def send_request(self, url:str, params:dict)->dict:
        try:
            response = requests.post(url, json=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(str(e))
            return {}