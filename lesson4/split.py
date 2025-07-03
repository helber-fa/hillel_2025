from lesson3.sequences import my_list

string = "Would you tell me,  please, which way Alex I ought  to go  from here?"

print(string.split(","))
print(string.split(" "))
print(string.split())

my_list = string.split()
print(type(string.split()))

# for element in my_list:
#     print(element)
#
# if "Alex" in my_list:
#     print("Text has word Alex inside")



