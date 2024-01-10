#!/usr/bin/env python3
class Person(object):

##constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

##check if this person is an employee
    def Display(self):
        print(self.name, self.id)

###driver code

emp = Person("Stephen\n", 347) ###an object of person
emp.Display()
