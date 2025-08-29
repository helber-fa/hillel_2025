from simple_iterator import SimpleRangeIterator
list_of_numbers = [11,12,13,14,15]
list_of_numbers2 = [21,22,23,24,25]
for elem in range(10):
    print(elem)

iter_obj = iter(list_of_numbers)
simple_iter_obj1 = iter(SimpleRangeIterator(10))
simple_iter_obj2 = SimpleRangeIterator(10).__iter__()

# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj2))
# print(next(iter_obj2))
# print(next(iter_obj2))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

try:
    while True:
        print(next(iter_obj))
except StopIteration:
    pass