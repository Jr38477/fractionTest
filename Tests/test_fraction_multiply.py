from fraction import Fraction
import unittest

class test_fraction_multiply(unittest.TestCase):
    def test_multiply_basic(self):
        """Test basic multiplication of two positive fractions"""
        a = Fraction(1, 2)
        b = Fraction(2, 3)
        result = a * b
        self.assertEqual(1, result.numerator)
        self.assertEqual(3, result.denominator)
    
    def test_multiply_whole_numbers(self):
        """Test multiplication resulting in a whole number"""
        a = Fraction(2, 3)
        b = Fraction(3, 2)
        result = a * b
        self.assertEqual(1, result.numerator)
        self.assertEqual(1, result.denominator)
    
    def test_multiply_by_one(self):
        """Test that multiplying by 1/1 returns the same fraction"""
        a = Fraction(5, 7)
        b = Fraction(1, 1)
        result = a * b
        self.assertEqual(5, result.numerator)
        self.assertEqual(7, result.denominator)
    
    def test_multiply_by_zero(self):
        """Test that multiplying by 0/1 returns 0/1"""
        a = Fraction(5, 7)
        b = Fraction(0, 1)
        result = a * b
        self.assertEqual(0, result.numerator)
        self.assertEqual(1, result.denominator)
    
    def test_multiply_negative_fractions(self):
        """Test multiplication of negative fractions"""
        a = Fraction(-1, 2)
        b = Fraction(2, 3)
        result = a * b
        self.assertEqual(-1, result.numerator)
        self.assertEqual(3, result.denominator)
    
    def test_multiply_two_negative_fractions(self):
        """Test that multiplying two negative fractions gives a positive result"""
        a = Fraction(-1, 2)
        b = Fraction(-2, 3)
        result = a * b
        self.assertEqual(1, result.numerator)
        self.assertEqual(3, result.denominator)
    
    def test_multiply_reduces_fraction(self):
        """Test that the result is reduced to lowest terms"""
        a = Fraction(2, 4)
        b = Fraction(3, 6)
        result = a * b
        self.assertEqual(1, result.numerator)
        self.assertEqual(4, result.denominator)
    
    def test_multiply_large_numerators(self):
        """Test multiplication with larger numbers"""
        a = Fraction(5, 7)
        b = Fraction(11, 13)
        result = a * b
        self.assertEqual(55, result.numerator)
        self.assertEqual(91, result.denominator)
    
    def test_multiply_same_fraction(self):
        """Test squaring a fraction"""
        a = Fraction(3, 4)
        result = a * a
        self.assertEqual(9, result.numerator)
        self.assertEqual(16, result.denominator)
    
    def test_multiply_with_integer(self):
        """Test multiplying a fraction by an integer (if supported)"""
        a = Fraction(2, 3)
        result = a * 3
        self.assertEqual(2, result.numerator)
        self.assertEqual(1, result.denominator)
    
    def test_multiply_commutative(self):
        """Test that multiplication is commutative: a*b == b*a"""
        a = Fraction(2, 5)
        b = Fraction(3, 7)
        result1 = a * b
        result2 = b * a
        self.assertEqual(result1.numerator, result2.numerator)
        self.assertEqual(result1.denominator, result2.denominator)
    
    def test_multiply_associative(self):
        """Test that multiplication is associative: (a*b)*c == a*(b*c)"""
        a = Fraction(1, 2)
        b = Fraction(2, 3)
        c = Fraction(3, 4)
        result1 = (a * b) * c
        result2 = a * (b * c)
        self.assertEqual(result1.numerator, result2.numerator)
        self.assertEqual(result1.denominator, result2.denominator)

