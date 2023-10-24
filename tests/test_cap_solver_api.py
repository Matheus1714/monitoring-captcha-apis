from unittest.mock import MagicMock

import pytest

from src.utils.model.CaptchaCapSolverAPI import CaptchaCapSolverAPI


class TestCaptchaAntiCaptchaAPI:

    @pytest.fixture
    def api(self):
        api = CaptchaCapSolverAPI()
        api.send_request = MagicMock()
        return api

    def test_type_balance(self, api):
        balance = api.get_balance()
        assert isinstance(balance, float)

    def test_type_has_balance(self, api):
        has_balance = api.has_balance()
        assert isinstance(has_balance, bool)
