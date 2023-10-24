from .BaseModel import BaseModel

from abc import abstractclassmethod

class BaseResponseModel(BaseModel):
    @abstractclassmethod
    def send_request(self, url:str, params:dict)->dict:
        ...
