import requests
import logging
logger = logging.getLogger("RestBase")

class RestBase:
    @staticmethod
    def _execute_request(method, url, params=None, data=None, json=None, files=None, status_code=None, headers=None, cookies=None):
        response = getattr(requests, method)(url=url, params=params, data=data, json=json, files=files, headers=headers, cookies=cookies)

        logger.info(f"request was send to {method} {url} with params {params}"
                    f"\nResponse has status code {response.status_code}")

        if status_code is not None:
            assert response.status_code == status_code, (f"Expected status code {status_code} "
                                                         f"but was actual is {response.status_code}")

        return response