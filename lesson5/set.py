# Відсутні індекси, сортувати не можна, сталість елементів не гарантована, містить ЛИШЕ УНІКАЛЬНІ значення
from lesson4.string_example import another_sting

my_string = "Hello"

my_set = {1,2,"Den", "Alex", "Den", 2, 5, my_string}

print(my_set)
my_string = "Hi"
my_set.add(5)
my_set.add(7)

print(my_set)

my_set.remove("Den")
my_set.pop()
# my_set.remove("Den") # не можна
print(my_set)


