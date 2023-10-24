from src.utils.model.ResponseModel import ResponseModel

import pytest
import requests
from requests.exceptions import RequestException
import requests_mock

@pytest.fixture
def response_model_instance():
    return ResponseModel()

def test_send_request_successful(response_model_instance):
    with requests_mock.Mocker() as mocker:
        url = "https://example.com/api"
        params = {"key": "value"}

        mocker.post(url, json={"result": "success"}, status_code=200)

        response = response_model_instance.send_request(url, params)

        assert response == {"result": "success"}

def test_send_request_request_exception(response_model_instance):
    with requests_mock.Mocker() as mocker:
        url = "https://example.com/api"
        params = {"key": "value"}

        mocker.post(url, exc=RequestException("Mocked request exception"))

        response = response_model_instance.send_request(url, params)

        assert response == {}