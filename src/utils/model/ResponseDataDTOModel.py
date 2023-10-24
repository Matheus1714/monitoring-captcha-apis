import http

from .ResponseDTOModel import ResponseDTOModel


class ResponseDataDTOModel(ResponseDTOModel):

    def __init__(self, error: str = 0, status: int = http.HTTPStatus.OK, message: str = '', data: list = []) -> None:
        super().__init__(error, status, message)
        
        self.data = data

    def get_response(self)->dict:
        return {
            'data': self.data,
            **super().get_response(),
        }