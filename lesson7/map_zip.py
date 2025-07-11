my_description = "My    Name    is   Alex".split(" ")
my_description_2 = "My    Name    is   Alex Den".split(" ")
print(my_description)
mapped_list = list(map(len, my_description_2))
print(mapped_list)
print([len(k) for k in my_description])

print(pow(2, 5))

base_numbers = [2, 5, 4, 9, 10]
powers = [5,3,4,5]
numbers_powers = list(map(pow, base_numbers, powers))

print(numbers_powers)

print(list(zip(my_description, mapped_list)))

