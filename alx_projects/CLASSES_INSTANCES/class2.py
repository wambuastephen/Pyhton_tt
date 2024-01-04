#!/usr/bin/env python3
class Employee:
    def __init__(self, first, last, pay):
        """
        Initializes an Employee object with first name, last name, and salary.

        Parameters:
        first (str): The first name of the employee.
        last (str): The last name of the employee.
        pay (int): The salary of the employee.
        """
        ### Assign the provided parameters to instance variables
        self.first = first
        self.last = last
        self.pay = pay
        ### Generate an email based on the first and last name
        self.email = first + '.' + last + '@gmail.com'
    def fullname(self):
        """
        Returns the full name of the employee.
        Returns:
        str: The full name of the employee.
        """
        # Combines the first and last name to create the full name
        return '{} {}'.format(self.first, self.last)
# Creating instances of the Employee class        
emp_1 = Employee('Stephen', 'Wambua', 50000)
emp_2 = Employee('Zippy', 'Mimo', 60000)

# Printing the email addresses of the employees
print(emp_1.email)
print(emp_2.email)

# Printing the full names of the employees using the fullname() method
print(emp_1.fullname())
print(emp_2.fullname())


"""
Classes: In Python, classes are blueprints for creating objects. They define properties (attributes) and behaviors (methods) that objects of that class will have.

Methods: These are functions defined within a class and operate on instances of the class. fullname() is a method inside the Employee class that returns the full name of an employee.

Instances: Objects created from a class are instances of that class. emp_1 and emp_2 are instances of the Employee class, each holding different data (first name, last name, salary, etc.) but sharing the same structure and methods defined in the class.

The docstrings are added to describe the purpose of the class and its methods. Comments are provided to explain each line of code within the class. This code creates employee objects, assigns attributes like names and emails, and demonstrates the use of the fullname() method to retrieve a formatted full name.
"""
