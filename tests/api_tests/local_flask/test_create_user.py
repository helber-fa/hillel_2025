from faker import Faker

faker = Faker()

def test_create_user(flask_ctrl):
    response = flask_ctrl.create_student({"name":faker.name(), "score":50})
    print(response.text)

