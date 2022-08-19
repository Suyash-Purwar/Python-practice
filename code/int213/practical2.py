# Program to find factorial

from distutils.log import fatal


def factorial(n):
    res = 1
    for i in range(n, 1, -1):
        res = res * i
    return res

def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n-1)


def main():
    n = int(input("Enter the n:"))
    if n <= 0:
        print("Factorial does not exist")
    else:
        result = factorial(n)
        recursive_res = recursive_factorial(n)
        print("Factorial is: " + str(result))
        print("Return of recursive factorial is: " + str(recursive_res))

main()

