#!/usr/bin/env python3
import unittest
import calc
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(1, 5), 6)
        self.assertEqual(calc.add(1, -1), 0)

    def test_subtraction(self):
        self.assertEqual(calc.subtraction(10, 5), 5)
        self.assertEqual(calc.subtraction(1, 5), -4)
        self.assertEqual(calc.subtraction(1, -1), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(1, 5), 5)
        self.assertEqual(calc.multiply(1, -1), -1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(1, 5), 0.2)
        self.assertEqual(calc.divide(1, -1), -1)

if __name__ == "__main__":
    unittest.main()
