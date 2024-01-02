#!/usr/bin/env python3
#supply one function (factorial)
def factorial(n):
    import math
    if not n >= 0:  #check if number is not negative.
        raise ValueError("n must be >=0")
    if math.floor(n) != n: #check if its a wholenumber.
        raise ValueError("n must be exact integer")
    if n+1 == n: #catch a value like 1e300 #avoid super huge numbers
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
