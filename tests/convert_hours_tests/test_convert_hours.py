import logging

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
    def test_convert_hours_positive(self, function_input, expected_result):
        actual_result = convert_to_24_hour(function_input)
        logging.info(f"expected: {expected_result}, actual: {actual_result}")
        assert actual_result == expected_result


    @pytest.mark.parametrize('function_input', [AttributeError, AttributeError, AttributeError])
    def test_convert_hours(self, function_input):
        logging.warning("Pay attention it is negative test ")
        with pytest.raises(AttributeError):
            convert_to_24_hour(0)