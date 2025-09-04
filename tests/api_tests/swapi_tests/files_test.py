import requests

url = "https://lms.ithillel.ua/assets/favicon/apple-touch-icon.png"
response = requests.get(url)

with open("hillel_logo.png", "wb") as f:
    f.write(response.content)

with open("hillel_logo.png", "rb") as f:
    data = {"file_name":f.read()}

file_response = requests.post(url, files=data)
pass

