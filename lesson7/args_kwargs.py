# def sum_all_elements(el_list):
#     return sum(el_list)
#
# print(sum_all_elements(range(20)))

def sum_all_elements(double_arg, *numbers, ignore_arg=5, **kwargs):
    print("Numbers:", numbers)
    print("ignore_num", ignore_arg)
    print("Double_sum", double_arg)
    print("Kwargs", kwargs)
    numbers_without_ignore = [k for k in numbers if k != ignore_arg]
    numbers_sum = sum(numbers_without_ignore)
    numbers_sum = double_arg*2 + numbers_sum
    if kwargs.get("double_all") is True:
        return numbers_sum * 2
    return numbers_sum

# print(sum_all_elements(1,2))

list_of_numbers = list(range(10, 20))


# print(sum_all_elements(list_of_numbers)) # don't work
my_params = {"ignore_num":8, "double_all": False, "param": 30, "additional_ignore": [5,7,9]}

print(sum_all_elements(*list_of_numbers,  5, my_custom_param = 20))
print("-"*80)
print(sum_all_elements(5, *list_of_numbers, **my_params))
