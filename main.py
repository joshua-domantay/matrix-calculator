# Joshua Anthony Domantay
# Matrix Calculator
# 28 February 2021

import os

def clear():
    os.system("cls")

def printHeader():
    print("Matrix Operations")
    print("Addition = add")
    print("Subtraction = sub")
    print("Multiplication = mul")
    print("Boolean Product = bp")
    print("Exit = exit")

def pressEnter():
    input("\nPress 'enter' to continue. ")

def mAdd():
    pass

def mSubtract():
    pass

def mMultiply():
    pass

def mBooleanProduct():
    pass

# Main
while(True):
    clear()

    printHeader()
    operation = input("\nEnter operation: ")
    operation = operation.lower()

    if(operation == "exit"):
        break
    elif(operation == "add"):
        mAdd()
        pressEnter()
    elif(operation == "sub"):
        mSubtract()
        pressEnter()
    elif(operation == "mul"):
        mMultiply()
        pressEnter()
    elif(operation == "bp"):
        mBooleanProduct()
        pressEnter()
