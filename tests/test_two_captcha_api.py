import pytest
from unittest.mock import MagicMock
from src.utils.model.CaptchaTwoCaptchaAPI import CaptchaTwoCaptchaAPI

class TestCaptchaTwoCaptchaAPI:

    @pytest.fixture
    def api(self):
        api = CaptchaTwoCaptchaAPI()
        api.send_request = MagicMock()
        return api

    def test_type_balance(self, api):
        balance = api.get_balance()
        assert isinstance(balance, float)

    def test_type_has_balance(self, api):
        has_balance = api.has_balance()
        assert isinstance(has_balance, bool)