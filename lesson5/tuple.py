# Іммутабельний тип з індексацією

my_tuple = ("Alex", "Den", "Ivan", "Den")
empty_tuple = ()
one_element_tuple = (42,)

print(type(my_tuple))
print(type(empty_tuple))
print(type(one_element_tuple))

# print(my_tuple)  /виводиться як tuple
# print(my_tuple[0]) / можна взяти елемент по індексу
# print(my_tuple[1:]) / можна робити слайси

# alex_name, den_name, *other_names = my_tuple #розпаковка tuple
#
# print(my_tuple)
# print("_"*80)
# print(alex_name)
# print(den_name)
# print(other_names)
# print(ivan_name)

print(my_tuple.count("Den"))

# Приведення типів

my_name = "Oleksandr"
my_list = [1,2,3]

# my_name_as_tuple = tuple(my_name)
# my_list_as_tuple = tuple(my_list)
#
# print(my_name)
# print(my_name_as_tuple)
#
# print(my_list)
# print(my_list_as_tuple)
# tuple записує комірки пам'яті, зміна стрінги перезаписує значення в пам'яті тому для tuple значення не змінюється
string = "Hello"
another_tuple = (string, "Hi", my_list)
print(another_tuple)
string = "Hi"
my_list.append("Den")
print(another_tuple)




