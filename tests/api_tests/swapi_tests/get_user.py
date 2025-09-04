import requests


response = requests.get(url="https://swapi.info/api/people/1")

status_code = response.status_code
text = response.text
headers = dict(response.headers)

print("status code", status_code)
print("headers", headers)
print("text", text)
print(response.json())
