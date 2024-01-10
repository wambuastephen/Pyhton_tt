#!/usr/bin/env python3
#try unsafe operation in try block
try:        #This block contains the code where an exception might occur.
    print("code start")
    #unsafe operation perform
    print(1 / 0)   #This line tries to perform a division by zero, which raises a ZeroDivisionError.
except:     #If an error occurs in the try block, the code inside the except block executes.
    print("an error occurs")   #Prints "an error occurs" to the console when an exception (in this case, a division by zero) happens.
finally:     #This block of code always executes, regardless of whether an exception occurred or not.
    print("finally code")    # Prints "finally code" to the console after executing the try or except block.
