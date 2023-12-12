#!/usr/bin/env python3

age = int(input("Enter your age: "))  # Convert the user input to an integer

if age > 18 and age < 65:  # Using 'and' to check both conditions
    print("Adult")
elif age >= 13 and age <= 19:  # Using 'and' to check both conditions for being a teenager
    print("Teenager")
else:
    print("Child")
