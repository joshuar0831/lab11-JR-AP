# https://github.com/joshuar0831/lab11-JR-AP.git
# Partner 1: Joshua Rayen
# Partner 2: Alexandre Pery
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(0, 2), 2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-2, 1), -3)
        self.assertEqual(subtract(0, 1), -1)

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 7), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5.0)
        self.assertEqual(div(4, 20), 5.0)
        self.assertEqual(div(5, 0), 0.0)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(4, 16), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-2, 8)
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(6, 8), 10.0)


    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(16), 4.0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()