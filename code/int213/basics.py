# Program to find factorial

def factorial(n):
    res = 1
    for i in range(n, 1, -1):
        res = res * i
    return res


def main():
    n = int(input("Enter the n:"))
    if n <= 0:
        print("Factorial does not exist")
    else:
        result = factorial(n)
        print("Factorial is: " + str(result))

main()