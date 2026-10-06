from fraction import Fraction
import unittest


class TestFractionStr(unittest.TestCase):
    def test_display_fraction(self):
        a = Fraction(1, 2)
        self.assertEqual("1/2", str(a))

    def test_display_int(self):
        a = Fraction(4, 1)
        self.assertEqual("4", str(a))

    def test_display_neg(self):
        a = Fraction(-1, 2)
        self.assertEqual("-1/2", str(a))
