import requests
from typing import Optional
from easy_http_requests.easy_http_response import EasyHttpResponse


class EasyHttpRequest:
    def __init__(self, base_url: Optional[str] = None):
        self.base_url = base_url.rstrip("/") if base_url else ""

    def get(self, endpoint: str) -> EasyHttpResponse:
        response = self._make_request("GET", endpoint)
        return EasyHttpResponse(response)

    def _make_request(self, method: str, endpoint: str) -> requests.models.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}" if self.base_url else endpoint
        response = requests.request(method, url)
        return response
