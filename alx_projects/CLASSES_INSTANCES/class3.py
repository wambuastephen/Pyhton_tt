#!/usr/bin/env python3
class Employee:
    """A class to represent an employee."""
    num_of_emps = 0 ### Class variable to keep track of the number of employees
    raise_amount = 1.04 ### Class variable for the raise amount

    def __init__(self, first, last, pay):
        """
        Initialize an Employee object.
        Args:
        - first (str): First name of the employee.
        - last (str): Last name of the employee.
        - pay (int): Pay of the employee.
        """
        self.first = first ### Instance variable to store first name
        self.last = last ### Instance variable to store last name
        self.pay = pay ### Instance variable to store pay 
        self.email = first + '.' + last + '@gmail.com' ### Instance variable for email address

        Employee.num_of_emps += 1 ### Increment the number of employees

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """Apply a raise to the employee's pay."""
        self.pay = int(self.pay * self.raise_amount)
# Display the initial number of employees
print(Employee.num_of_emps)
# Create employee instances
emp_1 = Employee('Stephen', 'Wambua', 50000)
emp_2 = Employee('Zippy', 'Mimo', 60000)
# Display the updated number of employees after creating instances
print(Employee.num_of_emps)
