class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __del__(self):
        print(f"The {self.make} {self.model} object has been destroyed.")

my_car = Car("1","2")
a = 5
print(type(a))
print(type(my_car))
print(id(my_car))
# Знищення об'єкта та автоматичний виклик деструктора
# del my_car
#
# print(a)
