import random

my_dict = {"key": "value", "another_key": 1, "dict_key": {"sub_key": "sub_value"}}
print(my_dict)

my_dict["new_key"] = True
print(my_dict)

print(my_dict["dict_key"])
print(my_dict["dict_key"]["sub_key"])

my_dict["another_key"] = 2
print(my_dict)

new_dict = {"lonley_key": None, "key": "value_new"}
my_dict.update(new_dict)
print(my_dict)

# print(my_dict["non_exist"]) #видає помилку
# print(my_dict.get("non_exist")) # не видає помилку, повертає None

# a = 10
# b = 20
#
# print(a, b)
#
# a,b = b,a
# print(a,b)


age_name_dict = {
    "Alex": [20, "QA"],
    "Den": [25, "AQA"],
    "Ivan": [30, "Dev"]}
print(age_name_dict.keys())

for name in age_name_dict.keys():
    print(name)

for age in age_name_dict.values():
    print(age)

for name, info in age_name_dict.items():
    print(f"My name is {name} and I am {info[0]} years old and working as {info[1]}")

another_dict = {number_key: number_key ** 2 for number_key in range(10)}
print(another_dict)

number_name_dict = {
    number: random.choice(list(age_name_dict.keys()))
    for number in range(10, 20)
    if number != 15
}

print(number_name_dict)
