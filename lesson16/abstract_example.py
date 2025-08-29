from abc import ABC, abstractmethod

# Абстрактний клас тварини
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Клас собаки, що успадковує абстрактний клас Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Клас кота, що успадковує абстрактний клас Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
#
# some_animal = Animal()
# some_animal.make_sound()

# dog = Dog()
# print(dog.make_sound())