class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)
    #
    # def __sub__(self, other):


# Використання оператора додавання та автоматичний виклик __add__
point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1 + point2
print(result.x, result.y)  # Виведе: 4 6

