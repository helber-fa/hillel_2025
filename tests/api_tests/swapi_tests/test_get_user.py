import pytest

from core.api.swapi.swapi_controller import SwapiController



# @pytest.mark.swapi
# @pytest.mark.parametrize("user_id", [1, 2, 0], ids=["user_id_1", "user_id_2", "user_id_3"])
# def test_get_user(user_id):
#     response = SwapiController().get_person(user_id)
#     print(response.text)
#     assert response.text is not None

@pytest.mark.swapi
@pytest.mark.parametrize("user_id", [1, 2, 3], ids=["user_id_1", "user_id_2", "user_id_3"])
def test_get_user(user_id):
    response = SwapiController().get_person(user_id)
    assert response.text is not None
