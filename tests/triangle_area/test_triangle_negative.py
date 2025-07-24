import pytest

from test_functions import triangle_area

class TestTriangleNegative:

    @pytest.mark.xfail(reason="Should be fixed in ticket number 123")
    @pytest.mark.my_custom_mark
    def test_triangle_negative_0(self):
        assert triangle_area(0) == 0.4330127018922193

    @pytest.mark.my_custom_mark
    @pytest.mark.regression
    @pytest.mark.skip(reason="We run this test only on DEV")
    def test_triangle_negative(self):
        assert triangle_area(2,2,2) == 1.7320508075688771