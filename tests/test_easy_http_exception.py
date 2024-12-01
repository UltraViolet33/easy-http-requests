from easy_http_requests.exceptions.easy_http_error import EasyHttpRequestError


class TestEasyHttpException:

    def test_easy_http_request_error(self):
        error = EasyHttpRequestError("HTTP request failed")
        assert str(error) == "HTTP request failed"
        assert error.original_exception is None

    def test_easy_http_timeout_error(self):
        error = EasyHttpRequestError("The request timed out")
        assert str(error) == "The request timed out"
        assert error.original_exception is None

    def test_easy_http_connection_error(self):
        error = EasyHttpRequestError("Failed to connect to the server")
        assert str(error) == "Failed to connect to the server"
        assert error.original_exception is None

    def test_easy_http_request_error_with_original_exception(self):
        original_exception = Exception("Original exception")
        error = EasyHttpRequestError(
            "HTTP request failed", original_exception=original_exception
        )
        assert str(error) == "HTTP request failed"
        assert error.original_exception == original_exception
