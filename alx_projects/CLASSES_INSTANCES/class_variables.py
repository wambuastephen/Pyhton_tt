#!/usr/bin/env python3
class Employee:
    """
    Represents an employee with attributes and methods.
    Attributes:
    raise_amount (float): A class attribute indicating the raise percentage for all employees.
    first (str): The first name of the employee.
    last (str): The last name of the employee.
    pay (int): The salary of the employee.
    email (str): The email address of the employee.
    """
### Class attribute for raise amount
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        """
        Initializes an Employee object with first name, last name, and salary.
        Parameters:
        first (str): The first name of the employee.
        last (str): The last name of the employee.
        pay (int): The salary of the employee.
        """

        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        """
        Returns the full name of the employee.
        Returns:
        str: The full name of the employee.
        """
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """
        Applies a raise to the employee's salary based on the raise amount.
        The raise amount is a class attribute.
        """
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Stephen', 'Wambua', 50000)
emp_2 = Employee('Zippy', 'Mimo', 60000)

emp_1.raise_amount = 1.05 ### Changing raise_amount for emp_1 instance

print(emp_1.__dict__) ### Instance dictionary showing attributes specific to emp_1
print(emp_2.__dict__)
print(Employee.raise_amount)### Class attribute accessed through the class
print(emp_1.raise_amount) ### Instance attribute overridden for emp_1
print(emp_2.raise_amount) ### Default class attribute value for emp_2
##EMPLOYEE1
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
##EMPLOYEE2
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)


