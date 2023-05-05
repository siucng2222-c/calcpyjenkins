import unittest
from calculator import Calculator 
class TestCalculatorMethods(unittest.TestCase):

    def test_upper(self):
        calculator = Calculator()
        # self.assertEqual(3*4, 12)
        self.assertEqual(calculator.multipy(3,4), 1)


if __name__ == '__main__':
    unittest.main()