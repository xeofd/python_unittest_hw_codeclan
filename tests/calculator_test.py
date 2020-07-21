# import python test items
import unittest
from src.calculator import add, divide, multiply, subtract

# unit test class
class TestCalculator(unittest.TestCase):
    # test functions
    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_subtract(self):
        self.assertEqual(2, subtract(5, 3))

    def test_divide(self):
        self.assertEqual(3, divide(21, 7))
    
    def test_multiply(self):
        self.assertEqual(25, multiply(5, 5))