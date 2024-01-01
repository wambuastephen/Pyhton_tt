#!/usr/bin/env python3
def secret_number():
    secret_number = 7
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess == secret_number:
                print("You guesses right")
                break
            else:
                print("Wrong guess. Try again!")
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    secret_number()
"""
The else block and the except ValueError block serve different purposes within a try-except structure.

else block: This block is executed when no exception occurs inside the try block. In a try-except structure, if the code inside the try block runs successfully without raising any exceptions, the code inside the else block will execute. It's often used to perform actions that should only happen if no exceptions were raised. In your context, if the user's input doesn't result in a ValueError (i.e., it's successfully converted to an integer), and it's not equal to the secret number, the program will inform the user of the incorrect guess within the else block.

except ValueError block: This block catches specific exceptions, in this case, ValueError. When the code inside the try block raises a ValueError exception (for example, due to the user inputting a non-numeric value when int(input()) is executed), the program jumps to this block to handle that particular type of exception. In your code, if the input cannot be converted to an integer (raising a ValueError), the program informs the user to enter a valid number.

In summary, the else block is executed when no exceptions are raised, while the except ValueError block specifically handles ValueError exceptions that might occur within the try block. Both are used to control the flow of code based on whether exceptions occur during execution.
"""

