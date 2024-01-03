#!/usr/bin/env python3
from math import pi # Imports the constant pi from the math module
def circle_area(r):
    if type(r) not in [int, float]: # Checks if the type of 'r' is not a valid numeric type (int or float)
        raise TypeError("The radius mus be a non-negative real number.")

    if r < 0:  # Checks if the radius is negative
        raise ValueError("The radius cannot be negative.")
# Calculates the area of the circle using the formula πr^2 and returns it:
    return pi*(r**2)
"""
#Test function
radii = [2, 0, -3, 2 + 5j, True, "radius"]
message = "Area of circles with r = {radius} is {area}."
for r in radii:
    A = circle_area(r)
    print(message.format(radius=r, area=A))
"""
