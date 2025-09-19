import sqlite3
import time
import pytest
import requests
from core.api.local_flask.local_flask_controller import LocalFlaskController
from constants import BASE_PATH

@pytest.fixture(scope="session")
def base_url():
    print("Calling base_url fixture")
    yield "http://127.0.0.1:8080"
    print("We can see this after session tests")

@pytest.fixture(scope="session", autouse=True)
def timing_of_all_tests():
    start_time = time.time()
    yield
    print(f"Time of all tests is {time.time()-start_time}")

@pytest.fixture(scope="package", autouse=True)
def print_logs_of_flask():
    yield
    print("Logs of this run")
    with open("requests_logs.log") as f:
        print(f.read())

@pytest.fixture(scope="session")
def auth_headers(base_url):
    token = requests.post(url=f"{base_url}/auth/", json={"name": "test", "password": "test"}).text
    return {"token": token}, base_url

@pytest.fixture(scope="session")
def flask_ctrl():
    return LocalFlaskController()

@pytest.fixture(scope="session")
def sql_cursor():
    conn = sqlite3.connect(f"{BASE_PATH}\core\local_server\ololo.db")
    cursor = conn.cursor()
    yield cursor
    conn.close()
