def addition(arr):
    sum = 0
    for i in arr:
        sum = sum + i

    return sum

def multiplication(arr):
    mul = 1
    for i in arr:
        mul = mul * i
    
    return mul

def main():
    n = int(input("Enter the size of the array:\n "))
    arr = []

    for i in range(n):
        element = int(input("Enter the digit: "))
        arr.append(element)

    result1 = multiplication(arr)
    result2 = addition(arr)

    print(result1, result2)

main()