#!/usr/bin/env python3

class Emp(Person):
    def Print(self):
        print("Emp class called")

Emp_details = Emp("Kalulu", 348)

###calling function class function
Emp_details.Display()

##calling child class function
Emp_details.print()
