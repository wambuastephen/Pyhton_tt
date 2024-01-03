#!/usr/bin/env python3
import unittest ## Imports the unittest module for testing
from circles import circle_area ## Imports the circle_area function from the circles module
from math import pi ## Imports the constant pi from the math module
class TestCircleArea(unittest.TestCase):## Defines a test case class that inherits from unittest.TestCase # # Defines a test method to check the calculation of circle areas
    def test_area(self):
        #Test area when radius is >= 0.
        self.assertAlmostEqual(circle_area(1), pi) ### Checks if the area of a circle with radius 1 is pi
        self.assertAlmostEqual(circle_area(0), 0) ### Checks if the area of a circle with radius 0 is 0
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2) ### Checks if the area of a circle with radius 2.1 is pi * (2.1^2)


    def test_values(self): ## Defines a test method to check value errors for negative radii
        # Make sure value errors are raised when necessary
        #make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2) ## Checks if a ValueError is raised when radius is -2
    def test_types(self): ## Defines a test method to check type errors for non-real number inputs
                # Make sure errors are raised when input is not a real number
        #make sure errors raised when input is not a real number
        self.assertRaises(TypeError, circle_area, 3+5j) ## Checks if a TypeError is raised when radius is a complex number
        self.assertRaises(TypeError, circle_area, True) ## Checks if a TypeError is raised when radius is a boolean
        self.assertRaises(TypeError, circle_area, "radius") ## Checks if a TypeError is raised when radius is a string


if __name__ == '__main__': ## Runs the tests if this script is executed directly
    unittest.main() ## Executes the tests using the unittest module
