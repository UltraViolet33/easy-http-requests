from unittest.mock import patch, MagicMock
from requests.models import Response
from easy_http_requests.easy_http_request import EasyHttpRequest
from easy_http_requests.easy_http_response import EasyHttpResponse
from requests.structures import CaseInsensitiveDict


class TestEasyHttpRequest:

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

        mock_request.assert_called_once_with("GET", "https://api.example.com/endpoint")
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

        mock_request.assert_called_once_with("GET", "https://api.example.com/endpoint")
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

        mock_request.assert_called_once_with("GET", "endpoint")
        assert response.status_code == 200
        assert response.body == {"key": "value"}
        assert response.text == '{"key": "value"}'

    @patch("requests.request")
    def test_get_failure(self, mock_request):
        mock_request.side_effect = Exception("HTTP request failed")

        client = EasyHttpRequest(base_url="https://api.example.com")
        try:
            client.get("endpoint")
        except Exception as e:
            assert str(e) == "HTTP request failed"
            assert isinstance(e, Exception)

    @patch("requests.request")
    def test_get_timeout(self, mock_request):
        mock_request.side_effect = TimeoutError("The request timed out")

        client = EasyHttpRequest(base_url="https://api.example.com")
        try:
            client.get("endpoint")
        except TimeoutError as e:
            assert str(e) == "The request timed out"
            assert isinstance(e, TimeoutError)

    @patch("requests.request")
    def test_get_connection_error(self, mock_request):
        mock_request.side_effect = ConnectionError("Failed to connect to the server")

        client = EasyHttpRequest(base_url="https://api.example.com")
        try:
            client.get("endpoint")
        except ConnectionError as e:
            assert str(e) == "Failed to connect to the server"
            assert isinstance(e, ConnectionError)

    @patch("requests.request")
    def test_easy_http_request_returns_easy_http_response(self, mock_request):
        mock_response = MagicMock(spec=Response)
        mock_request.return_value = mock_response

        client = EasyHttpRequest(base_url="https://api.example.com")
        response = client.get("endpoint")

        assert isinstance(response, EasyHttpResponse)
        assert response.response == mock_response
