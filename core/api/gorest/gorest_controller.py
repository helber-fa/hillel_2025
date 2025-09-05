from core.api.rest_base import RestBase


class GorestController(RestBase):
    def __init__(self, url="https://gorest.co.in/public/v2"):
        self.url = url
        self.token = self.get_token()

    def get_token(self):
        return "19ed479ee907709b391a0315fdfed5e1756f6a8fb607913415413b6c4a7a9c1d"

    def create_user(self, data, status_code=201):
        url = f"{self.url}/users"
        return self._execute_request(method="post", url=url, data=data,
                                     headers={"Authorization": f"Bearer {self.token}"}, status_code=status_code)
