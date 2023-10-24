from .ResponseModel import ResponseModel
from abc import abstractclassmethod

class BaseCaptchaResponseModel(ResponseModel):
    base_url:str = ''
    api_key:str = ''

    @abstractclassmethod
    def set_api_key(self, api_key: str)->None:
        ...

    @abstractclassmethod
    def get_url_balance(self)->str:
        ...

    @abstractclassmethod
    def get_balance(self)->float:
        ...
    
    @abstractclassmethod
    def has_balance(self)->bool:
        ...