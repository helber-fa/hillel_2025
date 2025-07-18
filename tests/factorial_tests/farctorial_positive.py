import unittest

import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from test_functions import factorial


# print(f"file path: {pathlib.Path(__file__)}")
# print(f"root path: {pathlib.Path(__file__).parent.parent.parent}")


class FactorialPositiveTest(unittest.TestCase):
    def test_factorial_5(self):
        actual_result = factorial(5)
        expected_result = 120

        self.assertEqual(expected_result, actual_result)

    def test_factorial_0(self):
        actual_result = factorial(0)
        expected_result = 1

        self.assertEqual(expected_result, actual_result)

if __name__ == ("__main__"):
    unittest.main(verbosity=2)