import requests
import logging

from core.api.rest_base import RestBase

logger = logging.getLogger("swapi_controller")


class SwapiController(RestBase):
    def __init__(self, url="https://swapi.info/api"):
        self.url = url

    def get_person(self, user_id):
        url = f"{self.url}/people/{user_id}"
        return self._execute_request(method="get", url=url)

    def get_planet(self, planet_id):
        url = f"{self.url}/planet/{planet_id}"
        return self._execute_request(method="get", url=url)


    def get_people(self):
        pass