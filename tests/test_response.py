import pytest
import requests_mock
from requests.exceptions import RequestException

from src.utils.model.ResponseModel import ResponseModel


class TestResponseModel:

    @pytest.fixture
    def response_model(self):
        return ResponseModel()

    def test_send_request_successful(self, response_model):
        with requests_mock.Mocker() as mocker:
            url = "https://example.com/api"
            params = {"key": "value"}

            mocker.post(url, json={"result": "success"}, status_code=200)

            response = response_model.send_request(url, params)

            assert response == {"result": "success"}

    def test_send_request_request_exception(self, response_model):
        with requests_mock.Mocker() as mocker:
            url = "https://example.com/api"
            params = {"key": "value"}

            mocker.post(url, exc=RequestException("Mocked request exception"))

            response = response_model.send_request(url, params)

            assert response == {}