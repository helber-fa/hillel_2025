import pytest

from test_functions import triangle_area
from utils import is_dev


class TestTrianglePositive:

    @pytest.mark.my_custom_mark
    @pytest.mark.smoke
    def test_triangle_1_1_1(self):
        assert triangle_area(1,1,1) == 0.4330127018922193

    @pytest.mark.smoke
    @pytest.mark.skipif(not is_dev(), reason="On DEV only")
    def test_tria_2_2_2(self):
        assert triangle_area(2, 2, 2) == 1.7320508075688772


