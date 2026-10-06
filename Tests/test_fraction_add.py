import unittest
from fraction import Fraction

class Test_fraction_addition(unittest.TestCase):

    def test_addition_basic(self):

    a = fraction(1,2)
    b = fraction(1,3)
    result = a + b

    self.assertEqual(5,result.numberator)
    self.assertEqual(6.result.denominator)


    def test_addition_by_zero(self):
      a = fraction(2,3)
      b = fraction(0,1)

      result = a + b

      self.assertEquals(2,result.numberator)
      self.assertEquals(3,result.denominator)

    def test_addwhole(self):

      a = fraction(2,3)
      b = fraction(1,3)

       result = a + b

      self.assertEquals(1,result.numberator)
      self.assertEqauls(1,result.denominator)

    def addtion_by_one_test(self):
      a = fraction(1,3)
      b = fraction(1,1)

      result = a + b

      self.assertEqauls(4,result.numberator)
      self.assertEquals(3,result.denominator)

    def addtion_by_neg_test(self)


    a = fraction(-1,3)
    b = fraction(1,3)

    result = a + b

    self.assertEqauls(0,result.numberator)
    self.assertEquals(0,result.denominator)

    

  
