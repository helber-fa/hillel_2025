numbers_list = [5,9,-9,14,-78,0]
names_list = ["Den", "den", "Alex", "саша", "ivan", "Zoya"]

numbers_sorted = sorted(numbers_list, reverse=True) # не змінює список
names_sorted = sorted(names_list) # не змінює список

print(names_sorted)
print(numbers_sorted)
numbers_list.sort() # змінює список
names_list.sort() # змінює список
print(numbers_list)
print(names_list)