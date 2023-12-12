#!/usr/bin/env python3
first = "kalulu"
last = "wambua"
full = first + ' ' + last
print(full)

#we can use a better method.
first = "kalulu"
last = "wambua"
full = f"{first} {last}"# Creates the full name using formatted strings
# you can put any value of expressions in { }
full = f"{len(first)} {2 + 2}"# Demonstrates using expressions within f-strings
print(full)# This will display the formatted full name
