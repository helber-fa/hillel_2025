class Animal:
    def make_sound(self):
        print("Animal sound")

class Lion(Animal):
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def make_sound(self):
        print("Rrrrrr")

class Bird(Animal):
    def __init__(self, name):
        self.name = name
        self.wings = 2

    def do_flying(self):
        print("flying...")

class Baran(Animal):
    def __init__(self, name):
        self.name = name
        self.horns = 2
        self.legs = 2

class Hymera(Lion, Bird, Baran):
    def __init__(self, name):
        self.name = name
        Bird.__init__(self, name)
        Lion.__init__(self, name)
        Baran.__init__(self, name)


hymera = Hymera("Bobic")
hymera.do_flying()
hymera.make_sound()
print(Hymera.mro())
print(hymera.name)
print(hymera.horns)
print(hymera.wings)
print(hymera.legs)