#!/usr/bin/env python3

def samp_string():
    return "This is a very important string"

if __name__ == "__main__":
    result = samp_string()
    print("Length:", len(result))
    print(result[4])  # Slicing from index 0
    print(result[0:6])  # Slicing
    print(result[7:14])  # Slicing of string
    print("This" + " is" + " a" + " very")  # Concatenation
for char in result: #Iterating through the characters of the string
    print(char)
for i in range(0, len(result)-1, 2):
    print(result[i] + result[i+1])
