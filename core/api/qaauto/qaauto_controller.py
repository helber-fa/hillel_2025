from core.api.rest_base import RestBase
from core.api.schemas.schema import CurrentSchema


class QAAutoController(RestBase):
    def __init__(self, url="https://qauto.forstudy.space/api"):
        self.url = url
        self.cookies = None

    def login(self, status_code=200, json=None):
        url = f"{self.url}/auth/signin"
        response = self._execute_request(method="post", url=url, status_code=status_code, json=json)
        self.cookies = dict(response.cookies)

    def get_current(self, status_code=200, uses_cookies=True):
        url = f"{self.url}/users/current"
        cookies = self.cookies if uses_cookies else None
        response = self._execute_request(method="get", url=url, cookies=cookies, status_code=status_code)
        CurrentSchema().load(response.json())
        return response