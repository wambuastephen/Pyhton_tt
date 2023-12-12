#!/usr/bin/env python3
# Example 1: range(stop)
#Generates a sequence from 0 up to (but not including) the specified stop value.
#For example: range(5) generates numbers 0, 1, 2, 3, 4 (but not 5).
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Example 2: range(start, stop)
#Generates a sequence starting from start up to (but not including) the specified stop value.
#For example: range(2, 7) generates numbers 2, 3, 4, 5, 6 (but not 7).
for i in range(2, 7):
    print(i)
# Output: 2, 3, 4, 5, 6

# Example 3: range(start, stop, step)
#Generates a sequence starting from start, up to (but not including) the specified stop value, incrementing by step.
#For example: range(1, 10, 2) generates numbers 1, 3, 5, 7, 9.

for i in range(1, 10, 2):
    print(i)
# Output: 1, 3, 5, 7, 9


#Key Points:
#range() by default starts at 0 if no start value is provided.
#It generates numbers up to, but not including, the stop value.
#The step parameter is optional. If not provided, it defaults to 1.
