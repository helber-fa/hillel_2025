numbers_list = [5,9,-9,14,-78,0]
names_list = ["Den", "den", "Alex", "саша", "ivan", "Zoya", "Aa", "ZZZZZZZZZ", "Z"]

numbers_sorted = sorted(numbers_list, reverse=True) # не змінює список
names_sorted = sorted(names_list) # не змінює список
sorted_by_lambda = sorted(names_list, key=lambda x: len(x))

def sort_fn(word):
    word_length = len(word)
    return word_length

sorted_by_fn = sorted(names_list, key=sort_fn)

print(names_sorted)
print(numbers_sorted)
numbers_list.sort() # змінює список
names_list.sort() # змінює список
print(numbers_list)
print(names_list)
print(sorted_by_lambda)
print(sorted_by_fn)