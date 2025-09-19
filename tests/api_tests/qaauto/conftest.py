from pytest import fixture
from core.api.qaauto.qaauto_controller import QAAutoController

@fixture(scope='session')
def qa_auto_ctrl():
    yield QAAutoController()

@fixture(scope='session', autouse=True)
def login(qa_auto_ctrl):
    print("send request to login")
    qa_auto_ctrl.login(json=
        {
            "email": "AutoQA_test12345@test.com",
            "password": "Qwerty12345",
            "remember": False
        }
    )
