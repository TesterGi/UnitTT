import unittest
from calculator import Calculator
class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.calculator = Calculator()
  #Each test method starts with the keyword test_
  def test_addition(self):
     self.assertEqual(Calculator.addition(2, 4), 6)
if __name__ == "__main__":
  unittest.main()
