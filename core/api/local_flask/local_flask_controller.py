from core.api.rest_base import RestBase


class LocalFlaskController(RestBase):
    __headers = None

    def __init__(self, url="http://127.0.0.1:8080"):
        self.url = url
        self.auth()

    def auth(self, status_code=200):
        if __class__.__headers is not None:
            return
        url = f"{self.url}/auth/"
        name = "test"
        password = "test"
        response = self._execute_request(method="post", url=url, json={"name": name, "password": password},
                                         status_code=status_code).text
        __class__.__headers = {"token": response}

    def get_students(self, status_code=200):
        url = f"{self.url}/students/"
        return self._execute_request(method="get", url=url, status_code=status_code)

    def get_student(self, student_id: int, status_code=200):
        url = f"{self.url}/students/{student_id}"
        return self._execute_request(method="get", url=url, status_code=status_code)

    def create_student(self, json_body: dict, status_code=201):
        url = f"{self.url}/students/"
        return self._execute_request(method="post", url=url, json=json_body,
                                     headers=self.__headers, status_code=status_code)
