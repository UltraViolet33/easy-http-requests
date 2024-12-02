from unittest.mock import patch, MagicMock
from requests.models import Response
from easy_http_requests.easy_http_request import EasyHttpRequest
from requests.structures import CaseInsensitiveDict
from tests.test_easy_http import TestEasyHttp


class TestEasyHttpPostRequest(TestEasyHttp):
    BASE_URL = "https://api.example.com"

    @patch("requests.request")
    def test_make_post_request(self, mock_request):
        mock_response = MagicMock(spec=Response)
        mock_request.return_value = mock_response

        client = EasyHttpRequest(base_url=self.BASE_URL)
        response = client._make_request("POST", "endpoint")

        mock_request.assert_called_once_with(
            "POST",
            "https://api.example.com/endpoint",
            params=None,
            data=None,
            json=None,
        )
        assert response == mock_response

    @patch("requests.request")
    def test_post_success(self, mock_request):
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 201
        mock_response.headers = CaseInsensitiveDict(
            {"Content-Type": "application/json"}
        )
        mock_response.json.return_value = {"key": "value"}
        mock_response.text = '{"key": "value"}'

        mock_request.return_value = mock_response

        client = EasyHttpRequest(base_url=self.BASE_URL)
        response = client.post("endpoint", json={"key": "value"})

        mock_request.assert_called_once_with(
            "POST",
            "https://api.example.com/endpoint",
            json={"key": "value"},
            params=None,
            data=None,
        )
        assert response.status_code == 201
        assert response.headers == {"Content-Type": "application/json"}
        assert response.body == {"key": "value"}
        assert response.text == '{"key": "value"}'

    @patch("requests.request")
    def test_post_request_form_params(self, mock_request):
        mock_response = MagicMock(spec=Response)
        mock_request.return_value = mock_response

        client = EasyHttpRequest(base_url=self.BASE_URL)
        response = client._make_request("POST", "endpoint", params={"key": "value"})

        mock_request.assert_called_once_with(
            "POST",
            "https://api.example.com/endpoint",
            params={"key": "value"},
            data=None,
            json=None,
        )
        assert response == mock_response

    @patch("requests.request")
    def test_post_request_no_base_url(self, mock_request):
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 201
        mock_response.json.return_value = {"key": "value"}
        mock_response.text = '{"key": "value"}'
        mock_request.return_value = mock_response

        client = EasyHttpRequest()
        response = client.post("endpoint", json={"key": "value"})

        mock_request.assert_called_once_with(
            "POST", "endpoint", json={"key": "value"}, params=None, data=None
        )
        assert response.status_code == 201
