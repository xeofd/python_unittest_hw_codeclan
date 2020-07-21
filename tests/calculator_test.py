# import python test items
import unittest
from src.calculator import add, divide, multiply, subtract

# unit test class
class TestCalculator(unittest.TestCase):
    # test functions
    def test_add(self):
        self.assertEqual(5, add(2, 3))