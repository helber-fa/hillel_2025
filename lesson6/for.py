# for number in range(10):
#     print(number)
#
# print(number)
#
names = ["Alex", "Den", "Ivan"]
# for _ in names:
#     print(_)


for name in names:
    print(name)
    for _ in range(10, 20, 2):
        print(_)

response = [
    {"id": 1, "name": "read_only", "description": "For all users"},
    {"id": None, "name": "RW", "description": "For read/write users"},
    {"id": 3, "name": "all", "description": "For admin"},
    {"id": 3, "name": "all", "description": "For admin"},
    {"id": None, "name": "broken", "description": None},
]
# continue - цикл переходить на наступну ітерацію
# break - виходимо з циклу чи умови
for permission in response:
    if permission.get("id") is None:
        print("Error: there is no id")
        break
    else:
        print("All work as expected")

names = ["Alex", "Den", "Ivan"]

for name in names:
    if name == "Den":
        print("I don't want to update Den")
        print(name)
        continue
    name = name + " updated"
    print(name)

# response_ids = [k.get("id") for k in response]
# if len(response_ids) != len(set(response_ids)):
#     print("Ids are not unique")
#
# print(response_ids)

