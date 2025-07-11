from lesson7.all_any import is_even

list_comp = [num for num in range(20) if is_even((num))]
print(list_comp)

# filter = filter(is_even, range(20))
print(list(filter(is_even, range(20))))
print(list(filter(is_even, [1,2,3,7,8,9,12])))\

my_description = "My    Name    is   Alex".split(" ")
print(my_description)

print([k for k in my_description if len(k)]) # => len(k) is True

res = []
for k in my_description:
    if len(k):
        res.append(k)
print(res)

print(list(filter(len,my_description)))