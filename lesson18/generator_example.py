# return повертає результат роботи чогось
# yield повертає проміжний результат

def get_name():
    return ["Alex", "Den", "Ivan"]
    print("Hello")

print(get_name())

def get_name_gen():
    print("Return Alex")
    yield "Alex"
    print("Return Den")
    yield "Den"
    print("Return Ivan")
    yield "Ivan"

for name in get_name_gen():
    print(name)

squares_generator = (x ** 2 for x in range(10))

for square in squares_generator:
    print(square)