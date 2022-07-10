import unittest
from calculator import Calculator
#Test cases to test Calulator methods
#You always create  a child class derived from unittest.TestCase
class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.calculator = Calculator()
  #Each test method starts with the keyword test_
  def test_multiply(self):
     self.assertEqual(Calculator.multiply(2, 4), 8)
if __name__ == "__main__":
  unittest.main()
