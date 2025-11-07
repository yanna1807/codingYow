#7/13/2024 and 7/14/2024
import math as m

print("Here's your calculator! Use it well..")
print("The operations are here: \nAdd = 2\nSubtract = 4\nMultiply = 6\nDivide = 8\nSquare_Root = 10\nExponent = 12")

add = 2
subtract = 4
multiply = 6
divide = 8
square_root = 10
exponent = 12

operation = input("Choose either add, subtract, multiply, divide, square_root or exponent: ")

def my_calcu():
    if operation == "2":
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your second number: "))
        number3 = int(input("Enter your third number: "))
        print("The sum of the three numbers you asked is: " + str(number1 + number2 + number3))
    elif operation == "4":
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your second number: "))
        print("The difference of the two numbers you asked is: " + str(number1 - number2))
    elif operation == "6":
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your second number: "))
        print("The product of the two numbers you asked is: " + str(number1 * number2))
    elif operation == "8":
        number1 = int(input("Enter your first number: "))
        number2 = int(input("Enter your second number: "))
        print("The quotient of the two numbers you asked is: " + str(number1 / number2))
    elif operation == "10":
        number = int(input("Enter your number: "))
        print("The square root of the number you asked is: %s"%m.sqrt(number))
    elif operation == "12":
        number = int(input("Enter your number: "))
        print("The exponent of 2 of the number you asked is: %d"%pow(number, 2))
    else:
        print("INVALID INPUT! Please choose whatever the instructions wants you to pick...")

my_calcu()

use_again = input("Do you want to use the calculator again: y/n? ")
if use_again == "y":
    operation = input("Choose either add, subtract, multiply, divide, square_root or exponent: ")
    my_calcu()
    use_again = input("Do you want to use the calculator again: y/n? ")
    if use_again == "y":
        operation = input("Choose either add, subtract, multiply, divide, square_root or exponent: ")
        my_calcu()
        use_again = input("Do you want to use the calculator again: y/n? ")
        if use_again == "y":
            operation = input("Choose either add, subtract, multiply, divide, square_root or exponent: ")
            my_calcu()
        else:
            print("Okay! I'll stop here then...")
else: 
    print("Goodbye! Just use the calculator next time! :)")

print("And that's it for now!")




