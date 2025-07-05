hardcoded_list = [1,2,3,4,5,7,9]

comrehended_list = []

# for num in hardcoded_list:
#     if num % 2 == 1:
#         comrehended_list.append(num ** 2)

comrehended_list = [num ** 2 for num in range(5, 20, 2) if num%2 ==1]

my_range = range(5, 20, 2)
print(list(my_range))

print(comrehended_list)

