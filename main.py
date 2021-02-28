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

def printMatrix(matrix, rows, cols):
    print("\nResult of Matrix operation")
    for i in range(rows):
        for j in range(cols):
            print(str(matrix[i][j]) + " ", end="")  
        print()

def getMatrixDimensions(matrixChar):
    rows = input("Matrix " + matrixChar + ", number of rows: ")
    cols = input("Matrix " + matrixChar + ", number of columns: ")
    if(not rows.isdigit() or not cols.isdigit()):
        print("\nERROR: At least one input is not a digit.")
        return -1, -1
    elif((int(rows) == 0) or (int(cols) == 0)):
        print("\nERROR: At least one input is equal to 0.")
        return -1, -1
    return int(rows), int(cols)

def getMatrixEmpty(rows, cols):
    matrix = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(0)
        matrix.append(col)
    return matrix

def getMatrix(matrixChar, rows, cols):
    matrix = []
    for i in range(rows):
        col = []
        for j in range(cols):
            x = input("Enter Matrix " + matrixChar + " row " + str(i) + " column " + str(j) + ": ")
            if(not x.isdigit()):
                print("\nERROR: Input is not a digit.")
                return -1
            col.append(int(x))
        matrix.append(col)
    return matrix

def mAdd(operation):
    # Get Matrix dimensions
    rowsA, colsA = getMatrixDimensions("A")
    if(rowsA == -1):
        return
    rowsB, colsB = getMatrixDimensions("B")
    if(rowsB == -1):
        return

    # Condition
    if((rowsA != rowsB) or (colsA != colsB)):
        print("\nERROR: Both Matrices do not have the same dimensions.")
        return

    # Get Matrix
    clear()
    matrixA = getMatrix("A", rowsA, colsA)
    if(matrixA == -1):
        return
    print()
    matrixB = getMatrix("B", rowsB, colsB)
    if(matrixB == -1):
        return
    matrixC = getMatrixEmpty(rowsA, colsB)

    # Calculation
    for i in range(rowsA):
        for j in range(colsA):
            x = 0
            if(operation == "add"):
                x = matrixA[i][j] + matrixB[i][j]
            else:
                x = matrixA[i][j] - matrixB[i][j]
            matrixC[i][j] = x
    
    clear()
    printMatrix(matrixC, rowsA, colsB)

def mMultiply(operation):
    # Get Matrix dimensions
    rowsA, colsA = getMatrixDimensions("A")
    if(rowsA == -1):
        return
    rowsB, colsB = getMatrixDimensions("B")
    if(rowsB == -1):
        return

    # Condition
    if(colsA != rowsB):
        print("\nERROR: The number of columns from Matrix A does not equal to the number of rows from Matrix B.")
        return

    # Get Matrix
    clear()
    matrixA = getMatrix("A", rowsA, colsA)
    if(matrixA == -1):
        return
    print()
    matrixB = getMatrix("B", rowsB, colsB)
    if(matrixB == -1):
        return
    matrixC = getMatrixEmpty(rowsA, colsB)

    # Calculation
    for i in range(rowsA):
        for j in range(colsB):
            x = 0
            for k in range(colsA):
                if(operation == "mul"):
                    x = x + (matrixA[i][k] * matrixB[k][j])
                else:
                    x = x | (matrixA[i][k] & matrixB[k][j])
            matrixC[i][j] = x

    clear()
    printMatrix(matrixC, rowsA, colsB)

# Main
while(True):
    clear()

    printHeader()
    operation = input("\nEnter operation: ")
    operation = operation.lower()

    if(operation == "exit"):
        break
    elif((operation == "add") or (operation == "sub")):
        mAdd(operation)
        pressEnter()
    elif((operation == "mul") or (operation == "bp")):
        mMultiply(operation)
        pressEnter()
