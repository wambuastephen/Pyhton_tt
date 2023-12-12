#!/usr/bin/env python3
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
message = "Eligible" if age >= 18 else "Not eligible"  #ternary operator.
print(message)

x = 5
result = "Even" if x % 2 == 0 else "Old"
print(result)

#nested ternary operator.
#while its concise, it should mantain readability.
x = 10
result = "Positive" if x > 0 else ("Zero" if x == 0 else "Negative")
print(result)
