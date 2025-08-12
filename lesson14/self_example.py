class Auto:
    def __init__(self, model, color, engine, fuel_to_km=0.2):
        self.model = model #поле інстансу
        self.color = color
        self.engine = engine
        self.tank = 0
        self.__fuel_to_km = fuel_to_km #протектед поле

    def drive_to_nearest_place(self, distance_km):
        if self.tank/self.__fuel_to_km >= distance_km:
            self.tank = self.tank - distance_km * self.__fuel_to_km
            print("Driving...")
        else:
            print(f"Can not go there, have fuel only for {self.tank/self.__fuel_to_km}")


class Nissan(Auto):
    brand = "NISSAN" # поле класу

    @classmethod
    def say_greeting(cls):
        print(f"Hello from {cls.brand}")

y61 = Nissan(model="y61", color="Green", engine="3.0", fuel_to_km=0.1)
navara = Nissan(model="navara", color="Black", engine="5.2")


y61.tank = 50
y61.drive_to_nearest_place(400)
y61.drive_to_nearest_place(400)
# Nissan.drive_to_nearest_place() # не спрацює
Nissan.say_greeting()

# y61_2 = Nissan(model="y61", color="Green", engine="3.0")


# print(y61.model)
# print(navara.model)
#
# print(y61.brand)
# print(navara.brand)
#
# print(y61.color)
# print(y61_2.color)
# print(id(y61.color))
# print(id(y61_2.color))



# print(id(y61.color))
# print(id(y61_2.color))

# y61_2.color = "Red"
# print(y61.color)
# print(y61_2.color)
#
# print(id(y61.color))
# print(id(y61_2.color))



