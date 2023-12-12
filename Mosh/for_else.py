#!/usr/bin/env python3
#for item in sequence:
# Code block executed for each item in the sequence
#if condition:
# Condition that, if met, breaks the loop
#break
#else:
# Code block executed if the loop completes without encountering a 'break'
# This block is not executed if the loop is prematurely terminated by a 'break'
#pass
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    if item == 6:
        break
else:
    print("Loop completed without encountering a break statement.")
