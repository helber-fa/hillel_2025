import unittest

def sum_2_numbers(a, b):
    return a + b


class MyTest(unittest.TestCase):
    def test_for_sum_1_2(self):
        actual_result = sum_2_numbers(1,2)
        expected_result = 3

        self.assertEqual(expected_result, actual_result)

    @unittest.skip("Test need to be done") # пропустити виконання цього тесту
    def test_sum_3_4(self):
        actual_result = [
            {
                "name": "Alex",
                "age": "29",
                "position": "AQA"
            },
            {
                "name": "Den",
                "age": "35",
                "position": "QA"
            },
            {
                "name": "Ivan",
                "age": "20",
                "position": "Dev"
            }
        ]
        expected_result = [
            {
                "name": "Alex1",
                "age": "29",
                "position": "AQA"
            },
            {
                "name": "Den",
                "age": "40",
                "position": "QA"
            },
            {
                "name": "Ivan",
                "age": "20",
                "position": "Qa"
            }
        ]

        self.assertEqual(actual_result, expected_result)

    def test_sum_assert(self):

        # actual_result = sum_2_numbers(3, 7)
        # expected_result = 7
        pop_up_is_displayed = False
        self.assertTrue(pop_up_is_displayed, msg="There is no pop up on the page")
        # self.assertAlmostEqual(actual_result, expected_result)

if __name__ == ("__main__"):
    unittest.main()