

my_dict = {"key":"value", "another_key":1, "dict_key":{"sub_key":"sub_value"}}
print(my_dict)

my_dict["new_key"] = True
print(my_dict)

print(my_dict["dict_key"])
print(my_dict["dict_key"]["sub_key"])

my_dict["another_key"] = 2
print(my_dict)

new_dict = {"lonley_key": None, "key":"value_new"}
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


