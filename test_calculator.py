import unittest
import calculator

class TestCalculator (unittest.TestCase):
  def test_addition(self):
    self.assertEqual(calculator.addition(5, 6), 11)
    self.assertEqual(calculator.addition(-5, 5), 0)
    self.assertEqual(calculator.addition(-5, -5), -10)
    self.assertEqual(calculator.addition(0, 0), 0)

  def test_subtraction(self):
    self.assertEqual(calculator.subtraction(11, 6), 5)
    self.assertEqual(calculator.subtraction(-5, 5), -10)
    self.assertEqual(calculator.subtraction(5, 5), 0)
    self.assertEqual(calculator.subtraction(0, 0), 0)
  
  def test_multiplication(self):
    self.assertEqual(calculator.multiplication(5, 5), 25)
    self.assertEqual(calculator.multiplication(-5, -1), 5)
    self.assertEqual(calculator.multiplication(5, -5), -25)
    self.assertEqual(calculator.multiplication(0, 0), 0)

  def test_division(self):
    self.assertEqual(calculator.division(25, 5), 5)
    self.assertEqual(calculator.division(-5, 1), -5)
    self.assertEqual(calculator.division(-25, -5), 5)
    self.assertEqual(calculator.division(0, 0), -1)

if __name__ == '__main__':
  unittest.main()