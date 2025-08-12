import pytest

class BaseValues:
    def get_data(self):
        return self.data

class PositiveValues(BaseValues):
    data = [1,2,3,4]


class NegativeValues(BaseValues):
    data = [None, False, 0, {0}]


@pytest.mark.parametrize("value", PositiveValues().get_data())
def test_positive_smthg(value):
    pass

@pytest.mark.parametrize("value", NegativeValues().get_data())
def test_negative_smthg(value):
    pass