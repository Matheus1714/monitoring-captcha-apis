from .BaseModel import BaseModel
import http

class ResponseDTOModel(BaseModel):

    def __init__(self, error:str = 0, status:int = http.HTTPStatus.OK, message:str = '') -> None:
        super().__init__()

        self.error = error
        self.status = status
        self.message = message
        
    def get_response(self)->dict:
        return {
            'error': self.error,
            'status': self.status,
            'message': self.message
        }