# {
#   "name": "John",
#   "lastName": "Dou",
#   "email": "AutoQA_test12345@test.com",
#   "password": "Qwerty12345",
#   "repeatPassword": "Qwerty12345"
# }
#

import requests

def test_something(qa_auto_ctrl):
    response_current = qa_auto_ctrl.get_current().json()
    assert response_current['status'] == 'ok'

# body = {
#   "email": "AutoQA_test12345@test.com",
#   "password": "Qwerty12345",
#   "remember": False
# }
#
# url_signin = "https://qauto.forstudy.space/api/auth/signin"
# url_get_current = "https://qauto.forstudy.space/api/users/current"
#
# session = requests.Session()
#
# # response_signin = requests.post(url=url_signin, json=body)
# response_signin = session.post(url=url_signin, json=body)
# # cookie = dict(response_signin.cookies)
# # print(cookie.get('sid'))
#
# # response_current = requests.get(url=url_get_current, cookies=cookie)
# response_current = session.get(url=url_get_current)
# print(response_current.json())
