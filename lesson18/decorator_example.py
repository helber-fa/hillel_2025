def greeting_decorator(fn):
    def wrapper(*args, **kwargs): # функція wrapper для додаткових дій
        print("Good morning")
        return fn(*args, **kwargs) # виклик основної функції
    return wrapper # виклик wrapper функції

@greeting_decorator
def greeting(name):
    print(f"Hello, {name}")


@greeting_decorator
def some_complex_logic_func(name, url, params=""):
    print(f"Hello, {name}")

greeting("Alex")
my_new_fn = greeting

my_new_fn("Den")

def new_greeting(name):
    print("Good morning")
    greeting(name)

greeting("Orest")
# print(id(my_new_fn))
# print(id(greeting))
#
# new_greeting("Ivan")






