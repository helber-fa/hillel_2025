string = "Would you tell me,  please, which way Alex I ought  to go  from here?"

print(string.startswith("Would"))
print(string.startswith("Could"))
print(string.endswith("here?"))
print(string.endswith("here."))

for word in string.split():
    print(f"is {word} starts with w: {word.startswith('w')}")

urls = ["www.page.com/users", "www.page.com/uses", "www.page.com/users2"]

for url in urls:
    if not url.endswith("/users"):
        print(f"Bad url - {url}")