class Animal:
    animal_type = "General Animal"

    def make_sound(self):
        print("Animal sound")

    def eat(self):
        print("Eating...")
    # def make_dog_sound(self):
    #     print("Woof")
    #
    # def make_cat_sound(self):
    #     print("Meow")

class Dog(Animal):
    animal_type = "Dog"
    def make_sound(self):
        print("Woof")

class Puppy(Dog):
    nice_name = "Barsic"

class Cat(Animal):
    animal_type = "Cat"
    def make_sound(self):
        print("Meow")

class Racoon(Animal):
    pass

dog = Dog()
dog.make_sound()
dog.eat()
print(dog.animal_type)


cat = Cat()
cat.make_sound()
cat.eat()
print(cat.animal_type)

racoon = Racoon()
print(racoon.animal_type)


barsic_puppy = Puppy()
print(barsic_puppy.nice_name)

barsic_puppy.make_sound()
barsic_puppy.eat()
#
# cat.make_dog_sound()