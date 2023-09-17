import unittest
from solution import sum_two_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = sum_two_numbers(5, 7)
        self.assertEqual(result, 12)

    def test_add_negative_numbers(self):
        result = sum_two_numbers(-3, -4)
        self.assertEqual(result, -7)

    def test_add_mixed_numbers(self):
        result = sum_two_numbers(10, -3)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
