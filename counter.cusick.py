# counter.cusick.py
# CIS - 135
# Assignment #13 Calculations



def addTwo():
    numOne = int(input("Please enter the first number to add: "))
    numTwo = int(input("Please enter the second number to add: "))
    sum = numOne + numTwo
    print("Adding: %d +, %d = %d" %(numOne, numTwo, sum))
    input("Press enter to continue... \n")
    return



def subtractTwo():
    numOne = int(input("\tPlease enter the first number to subtract: "))
    numTwo = int(input("\tPlease enter the second number to subtract: "))
    difference = numOne - numTwo
    print("Subtracting: %d - %d = %d" %(numOne, numTwo, difference))
    input("Press enter to continue... \n")
    return



def divideTwo():
    numOne = int(input("Please enter a number for the numerator: "))
    numTwo = int(input("Please enter a number for the denominator: "))
    quotient = numOne / numTwo
    print("Dividing %d %% %d = %d" %(numOne, numTwo, quotient))
    input("Press enter to continue... \n")
    return


def productTwo():
    numOne = int(input("PLease enter the first number to multiply: "))
    numTwo = int(input("Please enter the second number to multiply: "))
    product = numOne * numTwo
    print("Multiplying: %d * %d = %d" %(numOne, numTwo, product))
    input("Press enter to continue... \n")
    return

selection = 10
while selection != 0:
    print("\nGreetings! Welcome to the Python Calculator")
    print("Please make a selection from the menu below: ")
    print("\t Enter 1) Addition")
    print("\t Enter 2) Subtraction")
    print("\t Enter 3) Division")
    print("\t Enter 4) Multiplication")
    print("\t\t Enter 0 (zero) to exit")
    selection = int(input("Please make your selection: "))
    if (selection == 1):
        addTwo()
    elif (selection == 2):
        subtractTwo()
    elif (selection == 3):
        divideTwo()
    elif (selection == 4):
        productTwo()
    elif (selection == 0):
        print("Goodbye")
    else:
        print("Your input is not valid. Please try again.")
