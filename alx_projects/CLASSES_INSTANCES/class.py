#!/usr/bin/env python3
class Employee:
    """Initialize an Employee instance with their first name, last name, and salary."""
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com' ### Create the email address using first and last name
### Create instances of the Employee class
emp_1 = Employee('Stephen', 'Wambua', 50000)
emp_2 = Employee('Zippy', 'Mimo', 60000)

### Print the email addresses of the employees
print(emp_1.email)
print(emp_2.email)
print('{} {}'.format(emp_1.first, emp_1.last))
print('{} {}'.format(emp_2.first, emp_2.last))


def main():
    pass
if __name__ == "__main__":
    main()
###THIS IS A VERY LONG, TEDIOUS METHOD: REFER class2.py###
