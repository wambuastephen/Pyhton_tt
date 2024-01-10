#!/usr/bin/env python3

def get_numeric_input(prompt):
    """
    checks if users input is a valid number and not a string
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def triangle_side(a, b, c):
    """
    checks if a triangle is equilateral, isocelles or scalene.
    equilateral - all sides are equal
    isocelles - only two sides are equal
    scalene- neither side is equal to the other
    """
    
    if a == b == c:
        print ("Thats an Equilateral triangle")

    elif a == b or b == c or c ==a:
        print ("Thats Isocelles Triangle")

    else:
        print("Thats a scalene Triangle")

if __name__ == "__main__":
    side_a = get_numeric_input("Enter value of side a: ")
    side_b = get_numeric_input("Enter value of side b: ")
    side_c = get_numeric_input("Enter value of side c: ")
    
    triangle_side(side_a, side_b, side_c)
