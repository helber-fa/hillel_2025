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

first_set = {1,2,3}
second_set = {2,3,5,7}

print("_"*80)
union_set = first_set.union(second_set)
print(union_set)

intersection_set = first_set.intersection(second_set)
print(intersection_set)

difference_set = first_set.difference(second_set)
print(difference_set)

difference_set_second = second_set.difference(first_set)
print(difference_set_second)


sim_dif_set = first_set.symmetric_difference(second_set)
print(sim_dif_set)

third_set = {2,3,9}
print(third_set.issubset(first_set))



