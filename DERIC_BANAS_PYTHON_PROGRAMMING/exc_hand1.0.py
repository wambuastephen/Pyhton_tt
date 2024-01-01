#!/usr/bin/env python3
def number():
    while True:
        try:
            number = int(input("Please enter a number: "))
            break
        except ValueError:
            print("You didn't enter a number")
        except:
            print("An unknown error occurred")
    print("Thank You for entering a number")

if __name__ == "__main__":
    number()  # Call the number() function to start the input process

