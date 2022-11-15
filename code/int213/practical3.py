# Practice based on loop

# Print number from 1 to 100
def print1to100():
    for i in range(1, 100):
        print(i)
    print("")

# Program to print even numbers in range 1 to 100
def printEven1to100():
    for i in range(1, 101):
        if i%2 == 0:
            print(i)
    print("")

# Program to print descending list of 49 to 0
def printDesc49to0():
    for i in range(49, -1, -1):
        print(i)
    print("")

# Program to print odd number from 51 to 0
def printOdd51to0():
    for i in range(51, -1, -1):
        if i%2 != 0:
            print(i)
    print("")

# Program to print table of 5
def printFiveTable():
    for i in range(0, 51, 5):
        print(i)
    print("")

my_str = "I love python"
count = 0

for char in my_str:
    if char == "o":
        continue
    else:
        count = count + 1

print(count)
print(len(my_str))

print1to100()
printEven1to100()
printDesc49to0()
printOdd51to0()
printFiveTable()