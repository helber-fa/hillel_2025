import unittest

import sys
import pathlib
from unittest import expectedFailure

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from test_functions import factorial


class FactorialNegativeTest(unittest.TestCase):
    def test_factorial_minus_1(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_string(self):
        expected_message = "Int required"
        with self.assertRaises(TypeError) as typeError:
            factorial("string")
        exception = typeError.exception
        actual_message = exception.args[0]

        self.assertEqual(expected_message, actual_message)


if __name__ == ("__main__"):
    unittest.main()