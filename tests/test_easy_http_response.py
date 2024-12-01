from unittest.mock import patch, MagicMock
from requests.models import Response
from easy_http_requests.easy_http_response import EasyHttpResponse
from requests.structures import CaseInsensitiveDict


class TestEasyHttpResponse:

    def test_create_easy_http_response(self):
        mock_response = MagicMock(spec=Response)
        response = EasyHttpResponse(mock_response)
        assert response.response == mock_response

    def test_status_code(self):
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 200
        response = EasyHttpResponse(mock_response)
        assert response.status_code == 200

    def test_headers(self):
        mock_response = MagicMock(spec=Response)
        mock_response.headers = CaseInsensitiveDict(
            {"Content-Type": "application/json"}
        )
        response = EasyHttpResponse(mock_response)
        assert response.headers == {"Content-Type": "application/json"}

    def test_body(self):
        mock_response = MagicMock(spec=Response)
        mock_response.json.return_value = {"key": "value"}
        response = EasyHttpResponse(mock_response)
        assert response.body == {"key": "value"}

    def test_text(self):
        mock_response = MagicMock(spec=Response)
        mock_response.text = '{"key": "value"}'
        response = EasyHttpResponse(mock_response)
        assert response.text == '{"key": "value"}'
