import unittest
from solution import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add_numbers(5, 7)
        self.assertEqual(result, 12)
        print("The sum of 5 and 7 is",result)

    def test_add_negative_numbers(self):
        result = add_numbers(-3, -4)
        self.assertEqual(result, -7)
        print("The sum of -3 and -4 is",result)

    def test_add_mixed_numbers(self):
        result = add_numbers(10, -3)
        self.assertEqual(result, 7)
        print("The sum of 10 and -3 is",result)

if __name__ == '__main__':
    unittest.main()
