def findPerfectNumberInTheRange(num):
    sum = 0
    for i in range(1, num+1):
        a = 1
        while a < i:
            if i % a == 0:
                sum += a
            a+=1
        if (sum == i):
            print(str(i) + " is a perfect number")
        sum = 0

def printA(length, width):
    for i in range(0, length):
        if i == 0 or i == length/2:
            for j in range(0, width+1):
                print('*', end=" ")
        else:
            for j in range(0, width+1):
                if (j == 0 or j == width):
                    print('*', end=" ")
                else:
                    print(' ', end=" ")
        print("")

def main():
    # num = int(input("Enter the number: "))
    # findPerfectNumberInTheRange(num)
    # printA(8, 5)

    i = 0
    horsemen = ["war", True, not 0, 100, {"name": "Suyash"}]
    while i < len(horsemen):
        print(horsemen[i])
        i = i + 1

main()