# https://github.com/vsajinu/lab11-JN-FB/tree/main
# Partner 1: Jimmy Nguyen
# Partner 2: Fred Bertil

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(3, 7), -4)
        self.assertEqual(subtract(0, 0), 0)

######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 7), 0)

    def test_divide(self): # 3 assertions
        # divide(a, b) returns b / a
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(-4, 8), -2)
        self.assertAlmostEqual(divide(3, 1), 1 / 3)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(3, 27), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)
##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()