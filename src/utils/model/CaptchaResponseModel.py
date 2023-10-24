from settings import *

from .BaseCaptchaResponseModel import BaseCaptchaResponseModel
from .ResponseModel import ResponseModel


class CaptchaResponseModel(BaseCaptchaResponseModel):
    base_url:str = ''
    api_key:str = ''

    def set_api_key(self, api_key: str)->None:
        self.api_key = api_key
    