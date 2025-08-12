class Car:  #клас
    class_name = "Car" # поле класу

    def __init__(self, brand, model): #конструктор класу
        self.brand = brand # поле екземпляру
        self.model = model
        self.tank = 0

    def set_tank(self, value): # метод класу
        self.tank = value

    def go_somewhere(self, amount_in_km):
        if self.tank >= amount_in_km: #інкапсуляція
            self.tank = self.tank - amount_in_km
            print("Driving...")
        else:
            print("Can\'t go - have not enought fuel")

# class Car:
#     pass

x5 = Car(brand="BMW", model="X5") #instance чи екземпляр класу


print(x5.class_name)
print(x5.model)
print(x5.brand)
print(x5.tank)
x5.set_tank(50)
print(x5.tank)


# polo = Car(brand="VW", model="polo")
#
# print(polo.class_name)
# print(polo.model)
# print(polo.brand)