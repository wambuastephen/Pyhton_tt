#!/usr/bin/env python3
# x + 4 = 9. find value of x
def solve_eq(equation):
    parts = equation.split()
    num1 = 4
    num2 = 9

    if len(parts) != 4:
        return "Invalid equation format. Please provide an equation in the form 'x + num1 = num2'."
    x, operator, num1, num2 = parts

    if not (x.isalpha() and operator in ['+', '-', '*', '/'] and num1.isdigit() and num2.isdigit()):
        return "Invalid equation format. Please check your equation format."
    num1, num2 = int(num1), int(num2)

    if operator == '+':
        return f"x = {num2 - num1}"
    elif operator == '-':
        return f"x = {num2 + num1}"
    elif operator == '*':
        return f"x = {num2 / num1}" if num1 != 0 else "Cannot divide by zero."
    elif operator == '/':
        return f"x = {num2 * num1}"

    return "Equation solved."
print(solve_eq("x + num1 = num2"))

