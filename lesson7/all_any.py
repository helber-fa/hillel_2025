# print(all([True, True, False]))
# print(all([True, True]))

def is_even(number):
    return number % 2 == 0



# print(is_even(5))
# print(is_even(8))

result = [is_even(num) for num in [2,4,7]]

result_2 = []
for num in [2,4,6]:
    result_2.append(is_even(num))

print(result)
print(result_2)
#
# print(all(result))
# print(all(result_2))
#
# print(all([0, "Hi", 3]))

print(any(result))
print(any([0, "", 0]))

