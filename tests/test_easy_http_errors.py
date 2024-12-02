import requests
from unittest.mock import patch
from easy_http_requests.easy_http_request import EasyHttpRequest
from easy_http_requests.exceptions.easy_http_error import (
    EasyHttpRequestError,
    EasyHttpTimeoutError,
    EasyHttpConnectionError,
)
from tests.test_easy_http import TestEasyHttp


class TestEasyHttpErrors(TestEasyHttp):

    @patch("requests.request")
    def test_timeout_error_raises_custom_exception(self, mock_request):
        mock_request.side_effect = requests.exceptions.Timeout("The request timed out")

        with self.assertRaises(EasyHttpTimeoutError) as context:
            EasyHttpRequest(base_url=self.BASE_URL).get("endpoint")

        self.assertEqual(str(context.exception), "The request timed out")
        self.assertIsInstance(
            context.exception.original_exception, requests.exceptions.Timeout
        )

    @patch("requests.request")
    def test_connection_error_raises_custom_exception(self, mock_request):
        mock_request.side_effect = requests.exceptions.ConnectionError(
            "Failed to connect to the server"
        )

        with self.assertRaises(EasyHttpConnectionError) as context:
            EasyHttpRequest(base_url=self.BASE_URL).get("endpoint")

        self.assertEqual(str(context.exception), "Failed to connect to the server")
        self.assertIsInstance(
            context.exception.original_exception, requests.exceptions.ConnectionError
        )

    @patch("requests.request")
    def test_request_error_raises_custom_exception(self, mock_request):
        mock_request.side_effect = requests.RequestException("HTTP request failed")

        with self.assertRaises(EasyHttpRequestError) as context:
            EasyHttpRequest(base_url=self.BASE_URL).get("endpoint")

        self.assertEqual(str(context.exception), "HTTP request failed")
        self.assertIsInstance(
            context.exception.original_exception, requests.RequestException
        )
