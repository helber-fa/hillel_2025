import requests
import pytest

#session
#package
#module
#class
#function

def test_get_student_student_negative(base_url):
    print("test started")
    resp = requests.get(f"{base_url}/students/1").json()
    print(resp)
    assert isinstance(resp, dict)
    assert resp["id"] == 1