# має доступ по індексу
my_string = "HelloIamAlex"

# має доступ по індексу
my_list = [1, 2, 3, 4, 5, 6, 7, 865]

# не має доступу по індексу
my_set = {1, 2, 9, 1, "test", "test", 8, -2}

# має доступ по індексу
my_tuple = (1, 2, 3, "text")

# має доступ по ключу
my_dictionary = {"key": "value", 1: True}
# print(my_set)
# print(my_tuple)

# slices має 3 параметра [start:end:step]
print(my_string[0:len(my_string):2])

# індексація починається з 0
print(my_list[0])
print(my_list[1])

# повертає останній елемент
print(my_list[len(my_list)-1])

# виведе елементи ліста першого по п'ятий (з 0 по четвертий якщо по індексам)
print(my_list[0:5])

print(my_list[0:len(my_list)])

print(my_dictionary["key"])

print(min(my_list))
print(min(my_string))

print(max(my_list))
print(max(my_string))

print(sum(my_list))







