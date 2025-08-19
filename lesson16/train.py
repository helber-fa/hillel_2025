'''Опишіть об'єкт "Поїзд". Клас повинен містити поля та метод для додавання вагонів (необхідно додати об'єкти та екземпляри класу вагонів).
В поїзді завжди є 1 вагон і це локомотив (він не приймає пасажирів)
Опишіть клас Вагон разом з поїздом. Вагон повинен містити список пасажирів і дозволяти додавати пасажирів.
 У вагоні може бути не більше 10 пасажирів.
Під час використання функції len у вагоні я хочу бачити кількість пасажирів.
Використовуючи len у поїзді я хочу бачити список вагонів без локомотива. Кожен вагон повинен мати номер '''


class Person:
    def __init__(self, name):
        self.name = name

class Wagon:
    max_passengers=10
    def __init__(self, number:int, is_locomotive: bool):
        self.number = number
        self.is_locomotive = is_locomotive
        self.list_of_pass = []

    def add_passengers(self, new_passenger:Person):
        if self.is_locomotive:
            return
        if len(self.list_of_pass) < 10:
            self.list_of_pass.append(new_passenger)

    def __len__(self):
        return len(self.list_of_pass)


class Train:
    def __init__(self, name):
        self.locomotive = Wagon(number=1, is_locomotive=True)
        self.wagons = []
        self.name = name

    def add_wagon(self, new_wagon: Wagon):
        if not new_wagon.is_locomotive:
            self.wagons.append(new_wagon)

    def __len__(self):
        return len(self.wagons)

train = Train("Stefania")
first_wagon = Wagon(number=2, is_locomotive=False)
# first_wagon.add_passengers(Person("Alex"))
train.add_wagon(first_wagon)

print(train.wagons)
print(first_wagon.list_of_pass)
print(len(train))
print(len(first_wagon))
