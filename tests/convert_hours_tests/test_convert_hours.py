import pytest

from test_functions import convert_to_24_hour

# повторення коду
# @pytest.mark.convert_hours
# def test_convert_10_22():
#     assert convert_to_24_hour("10:22 AM") == "10:22"
#
# @pytest.mark.convert_hours
# def test_convert_1_34():
#     assert convert_to_24_hour("1:34 AM") == "01:34"
#
# @pytest.mark.convert_hours
# def test_convert_00_01():
#     assert convert_to_24_hour("00:01 AM") == "00:01"
@pytest.mark.convert_hours
class TestConvertHoursPositive:

    @pytest.mark.parametrize('function_input, expected_result', [
        ("10:22 AM", "10:22"),
        ("1:34 AM", "01:34"),
        ("00:01 AM", "00:01"),
    ])
    def test_convert_hours(self, function_input, expected_result):
        assert convert_to_24_hour(function_input) == expected_result


    @pytest.mark.parametrize('function_input', [ValueError, TypeError, IndexError])
    def test_convert_hours(self, function_input):
        with pytest.raises(AttributeError):
            convert_to_24_hour()