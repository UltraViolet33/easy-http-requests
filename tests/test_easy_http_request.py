from unittest.mock import patch, MagicMock
from requests.models import Response
from easy_http_requests.easy_http_request import EasyHttpRequest
from easy_http_requests.easy_http_response import EasyHttpResponse
from requests.structures import CaseInsensitiveDict
from tests.test_easy_http import TestEasyHttp


class TestEasyHttpRequest(TestEasyHttp):

    def test_create_easy_http_request(self):
        easy_http_request = EasyHttpRequest("base_url/")
        assert easy_http_request.base_url == "base_url"
        easy_http_request = EasyHttpRequest()
        assert easy_http_request.base_url == ""

    @patch("requests.request")
    def test_get_success(self, mock_request):
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 200
        mock_response.headers = CaseInsensitiveDict(
            {"Content-Type": "application/json"}
        )
        mock_response.json.return_value = {"key": "value"}
        mock_response.text = '{"key": "value"}'

        mock_request.return_value = mock_response

        client = EasyHttpRequest(base_url="https://api.example.com")
        response = client.get("endpoint")

        mock_request.assert_called_once_with(
            "GET",
            "https://api.example.com/endpoint",
            params=None,
            data=None,
            json=None,
            headers=None,
        )
        assert response.status_code == 200
        assert response.headers == {"Content-Type": "application/json"}
        assert response.body == {"key": "value"}
        assert response.text == '{"key": "value"}'

    @patch("requests.request")
    def test_make_get_request(self, mock_request):
        mock_response = MagicMock(spec=Response)
        mock_request.return_value = mock_response

        client = EasyHttpRequest(base_url="https://api.example.com")
        response = client._make_request("GET", "endpoint")

        mock_request.assert_called_once_with(
            "GET",
            "https://api.example.com/endpoint",
            params=None,
            data=None,
            json=None,
            headers=None,
        )
        assert response == mock_response

    @patch("requests.request")
    def test_get_no_base_url(self, mock_request):
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_response.text = '{"key": "value"}'
        mock_request.return_value = mock_response

        client = EasyHttpRequest()
        response = client.get("endpoint")

        mock_request.assert_called_once_with(
            "GET", "endpoint", params=None, data=None, json=None, headers=None
        )
        assert response.status_code == 200
        assert response.body == {"key": "value"}
        assert response.text == '{"key": "value"}'

    @patch("requests.request")
    def test_easy_http_request_returns_easy_http_response(self, mock_request):
        mock_response = MagicMock(spec=Response)
        mock_request.return_value = mock_response

        client = EasyHttpRequest(base_url="https://api.example.com")
        response = client.get("endpoint")

        assert isinstance(response, EasyHttpResponse)
        assert response.response == mock_response
