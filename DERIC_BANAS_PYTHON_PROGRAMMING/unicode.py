#!/usr/bin/env python3
#A - Z = 65 - 90
#a - z = 97 - 122
print("A =", ord("A")) ##This line prints the Unicode code point of the character 'A', which is 65. It's used to find the numeric value of a character in the Unicode table.
print("65 =", chr(65)) 
for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end='')
print()
for j in range(ord('A'), ord('Z') + 1):
    print(chr(j), end='')
print()
"""
This line prints the character corresponding to the Unicode code point 65, which is 'A'.It's used to find the character represented by a given numeric value in the Unicode table.
"""
"""
In Python, the ord() and chr() functions are used for converting between characters (letters, symbols) and their ASCII (or Unicode) representations.
"""
