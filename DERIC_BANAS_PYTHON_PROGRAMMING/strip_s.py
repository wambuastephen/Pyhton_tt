#!/usr/bin/env python3

def rand_string():
    rand_string = "      this is a very important string        "
    rand_string = rand_string.lstrip()
    rand_string = rand_string.rstrip()
    rand_string = rand_string.strip()
    rand_string = rand_string.capitalize()
    rand_string = rand_string.upper()
    rand_string = rand_string.lower()
    return rand_string

if __name__ == "__main__":
    modified_string = rand_string()
    print(modified_string)
    a_list = ["bunch", "of", "random", "words"]
    print(" ".join(a_list))
    a_list_2 = modified_string.split()
    for i in a_list_2:
        print(i)
    print("How many 'is':", modified_string.count("is"))
    print("Where is 'string':", modified_string.find("string"))

"""
lstrip(): Removes leading (left-side) whitespace characters. In the initial string, leading spaces before the text and spaces after the text are removed.
rstrip(): Removes trailing (right-side) whitespace characters. Since lstrip() has already removed leading spaces, this has no effect in this context.
strip(): Removes both leading and trailing whitespace characters. As there are no leading or trailing spaces left after the previous operations, this also has no additional effect.
Regarding the displayed outputs:

    print(rand_string.capitalize()): Capitalizes the first letter of the string and makes the rest lowercase. It doesn't affect whitespace.
    print(rand_string.upper()): Converts the entire string to uppercase. It doesn't affect whitespace.
    print(rand_string.lower()): Converts the entire string to lowercase. It doesn't affect whitespace.
    The reason why lstrip() and rstrip() are applied is to clean the string from any leading or trailing spaces before performing the capitalization, uppercasing, and lowercasing operations. However, strip() after lstrip() and rstrip() doesn't make any further changes as there are no leading or trailing spaces remaining at that point.
"""
