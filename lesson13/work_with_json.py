import json
#
user_data = [
    {"id": 1, "is_active": True, "friends": None, "name":"Alex"},
    {"id": 1, "is_active": True, "friends": None, "name": "Alex"},
    {"id": 1, "is_active": True, "friends":
        {"id": 1, "is_active": True, "friends": None, "name": "Alex"},
     "name": "Alex"}
]

# user_data = """[
#     {"id": 1, "is_active": True, "friends": None, "name":"Alex"},
#     {"id": 1, "is_active": True, "friends": None, "name": "Alex"},
#     {"id": 1, "is_active": True, "friends":
#         {"id": 1, "is_active": True, "friends": None, "name": "Alex"},
#      "name": "Alex"}
# ]"""

# user_data_json = json.dumps(user_data)
# print(user_data_json)
# print(type(user_data_json))

#
# with open('json_as_str.txt', 'w') as f:
#     f.write(user_data_json)
#
with open('json_as_json.json', 'w') as f:
    json.dump(user_data, f, indent=4)