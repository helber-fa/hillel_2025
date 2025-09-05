import time

from core.api.gorest.gorest_controller import GorestController

def test_create_user():
    user_data = {"name": "Oleksandr Rudyk",
                 "gender":"male",
                 "email": f"tenali.ramakrishna@{time.time()}.com",
                 "status": "active"}

    response = GorestController().create_user(data=user_data)
    pass
