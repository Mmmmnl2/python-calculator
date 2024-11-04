import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1,-2),-3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1,0),1)

    # Divide
    def test_div_negative(self):
        self.assertEqual(self.calc.divide(-4,-2),2)
    
    def test_div_normal(self):
        self.assertEqual(self.calc.divide(4,2),2)

    # def test_div_negative1(self):
    #     self.assertEqual(self.calc.multiply(4,-2),-2)

    # def test_div_negative2(self):
    #     self.assertEqual(self.calc.multiply(-4,2),-2)

    def test_div_zero(self):
        self.assertEqual(self.calc.divide(0,1),0)

    #Multiply
    def test_mul_negative(self):
        self.assertEqual(self.calc.multiply(-1,-2),2)

    def test_mul_negative1(self):
        self.assertEqual(self.calc.multiply(1,-2),-2)
    
    def test_mul_negative2(self):
        self.assertEqual(self.calc.multiply(-1,2),-2)
    
    def test_mul_negative3(self):
        self.assertEqual(self.calc.multiply(1,-4),-4)

    def test_mul_zero(self):
        self.assertEqual(self.calc.multiply(1,0),0)
    
    #Subtract
    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(-1,-4),3)

    def test_sub_zero(self):
        self.assertEqual(self.calc.subtract(1,0),1)

if __name__ == '__main__':
    unittest.main()