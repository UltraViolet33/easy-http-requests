import requests
from requests.structures import CaseInsensitiveDict


class EasyHttpResponse:
    def __init__(self, response: requests.models.Response):
        self.response = response

    @property
    def status_code(self) -> int:
        return self.response.status_code

    @property
    def headers(self) -> CaseInsensitiveDict[str]:
        return self.response.headers

    @property
    def body(self) -> dict:
        return self.response.json()

    @property
    def text(self) -> str:
        return self.response.text
