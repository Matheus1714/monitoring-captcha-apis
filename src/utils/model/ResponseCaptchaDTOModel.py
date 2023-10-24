import http
from .ResponseDTOModel import ResponseDTOModel

class ResponseCaptchaDTOModel(ResponseDTOModel):

    def __init__(self, error: str = 0, status: int = http.HTTPStatus.OK, message: str = '', balance = 0.0) -> None:
        super().__init__(error, status, message)
        
        self.balance = balance

    def get_response(self)->dict:
        return {
            'balance': self.balance,
            **super().get_response(),
        }