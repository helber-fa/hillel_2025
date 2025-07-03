my_full_name = "My name is Oleksandr Rudyk"

print(my_full_name.find("Oleksandr"))
print(my_full_name.find("s"))
print(my_full_name.find("Alex"))

if my_full_name.find("Oleksandr") > 0:
    print("There is Oleksandr in text")

print(my_full_name[:my_full_name.find("Oleksandr")])
print(my_full_name[my_full_name.find("Oleksandr"):])