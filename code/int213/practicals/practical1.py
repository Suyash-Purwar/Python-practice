# Code for the first practical
# Author: Suyash Purwar
# Date: 11/8/2022

def calculator(a, b, operator="all"):
    if operator == '+':
        print("a + b: " + str(a + b))
    elif operator == '-':
        print("a - b: " + str(a - b))
    elif operator ==  '*':
        print("a * b: " + str(a * b))
    elif operator == '/':
        print("a / b: " + str(a / b))
    elif operator == '**':
        print("a ** b: " + str(a ** b))
    elif operator == '//':
        print("a // b: " + str(a // b))
    elif operator == 'all':
        operators = ['+', '-', '*', '/', '**', '//']
        for op in operators:
            calculator(a, b, op)
    else:
        print("Unacceptable value received")

def main():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    operator = input("Enter the operator or just press enter if you want to perform all operations: ")

    if not operator:
        calculator(x, y, 'all')
    else:
        calculator(x, y, operator)

main()