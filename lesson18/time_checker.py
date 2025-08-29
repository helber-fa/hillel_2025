import random
import time
from time import sleep


# декоратор який буде обраховувати скільки часу виконувалась функція
def time_checker(fn):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f"Time spend: {end_time-start_time}")
        return result
    return wrapper

@time_checker
def function_spending_time():
    sleep(random.choice(range(10)))

for run in range(5):
    function_spending_time()