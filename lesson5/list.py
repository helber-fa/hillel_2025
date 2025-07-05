# Мутабельний тип з індексацією

my_list = [1,2,3, "Den", True, None, [5,6]]
# print(my_list)
# print(type(my_list))
# print(id(my_list))
my_list.append("Alex") # додаємо в кінець один елемент
# print(my_list)
# print(type(my_list))
# print(id(my_list))
sub_list = (0, -1)
my_list.append([0,-1])

my_list.extend(sub_list) # розширює список ітерабельними елементами
my_list.insert(1, "Ivan")

last_element = my_list.pop() # видаляє останній елемент і записує в змінну
den_name = my_list.pop(5) # видаляє елемент по індексу і записує в змінну

my_list.remove("Ivan")

print(my_list.index("Den"))
print(my_list.count("Den"))
print(my_list)


my_list[0], my_list[1] = my_list[1],my_list[0]
print(my_list)
# print(my_list[0])
# print(my_list[1:])
# print(my_list[-1])
# print(my_list[::-1])





