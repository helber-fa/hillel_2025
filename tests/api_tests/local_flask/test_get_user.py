import pytest
import requests
from faker import Faker
import random

from core.api.local_flask.local_flask_controller import LocalFlaskController

faker = Faker()
#session
#package
#module
#class
#function

def get_student_ids(user_number):
    ctrl = LocalFlaskController()
    student_ids = [k["id"] for k in ctrl.get_students().json()]
    random.shuffle(student_ids)
    return student_ids[:user_number]
desired_number = 5

@pytest.fixture(scope="session", params=get_student_ids(desired_number))
def student_id_parametrized(flask_ctrl, request):
    return request.param

def tests_get_student(flask_ctrl,student_id_parametrized):
    response = flask_ctrl.get_student(student_id_parametrized).json()
    assert isinstance(response, dict)
    assert response["id"] == student_id_parametrized

# def test_get_students(base_url):
#     print("test started")
#     resp = requests.get(f"{base_url}/students/").json()
#
#     assert resp != []
#     assert len(set([k["id"] for k in resp])) == len(resp)
#
# def test_get_student_student(base_url):
#     print("test started")
#     resp = requests.get(f"{base_url}/students/1").json()
#     print(resp)
#     assert isinstance(resp, dict)
#     assert resp["id"] == 1
#
# @pytest.mark.parametrize("student_id", range(1,11))
# def test_get_some_user(flask_ctrl, student_id):
#     response = flask_ctrl.get_student(student_id).json()
#     assert isinstance(response, dict)
#     assert response["id"] == student_id
#
# def test_db(flask_ctrl, sql_cursor):
#     response = flask_ctrl.create_student({"name": faker.name(), "score": 50}).json()
#     assert response.get('id') is not None
#
#     sql_cursor.execute(f"select * from student where id = {response.get("id")}")
#     db_user = sql_cursor.fetchone()
#     print(db_user)
