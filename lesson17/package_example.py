from lesson17 import User_class

from .module_example import Car
# from ..lesson16.animal_extended import hymera
from math import *
# from ..lesson16.animal_extended import hymera
from math import *

from lesson17 import User_class
from .module_example import Car


def test_user():
    user = User_class("Alex", 50)
    assert user.score == 50


# print(User_class("Alex", 50))
def test_car():
    car = Car("brand", "model")
    print(car)


# def test_dog():
#     print(hymera.make_sound())

def test_math():
    print(pi)
    # math.pi
