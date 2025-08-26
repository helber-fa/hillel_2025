import pytest
import pytest as pt

from pytest import mark
from pytest import mark as mk

from lesson14.car_object import Car

@pytest.mark.skip(reason="Example")
def test_example_modules():
    pass


@pt.mark.skip(reason="Example")
def test_example_modules_2():
    pass

@mark.skip(reason="Example")
def test_example_modules_3():
    pass

@mk.skip(reason="Example")
def test_example_modules_4():
    pass

@mk.skip(reason="Example")
def test_example_modules_4():
    Car("brand", "model")