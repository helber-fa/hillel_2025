from core.api.rest_base import RestBase

class SwapiController(RestBase):
    def __init__(self, url="https://swapi.info/api"):
        self.url = url

    def get_person(self, user_id, status_code=200):
        url = f"{self.url}/people/{user_id}"
        return self._execute_request(method="get", url=url, status_code=status_code)

    def get_planet(self, planet_id, status_code=200):
        url = f"{self.url}/planet/{planet_id}"
        return self._execute_request(method="get", url=url, status_code=status_code)


    def get_people(self):
        pass