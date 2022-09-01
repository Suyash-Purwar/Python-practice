import math

def solution1():
    nOfPlayers = int(input("Enter the number of players: "))
    scoresList = []

    for i in range(0, nOfPlayers):
        scores = input("Enter the scores: ")
        scoresList.extend([int(scores.split()[0]), int(scores.split()[1])])

    for j in range(0, nOfPlayers*2, 2):
        if scoresList[j] % scoresList[j+1] == 0:
            print(1)
        else:
            print(scoresList[j] % scoresList[j+1])

def solution2():
    # Each packet has 4 candies (Deduced from the sample i/o examples)
    nOfTestCases = int(input())
    childCandyList = []

    for i in range(0, nOfTestCases):
        childCandy = input()
        childCandyList.extend([int(childCandy.split()[0]), int(childCandy.split()[1])])

    for j in range(0, nOfTestCases*2, 2):
        print(j)
        child = childCandyList[j]
        candy = childCandyList[j+1]
        if child > candy:
            packets = math.ceil((child - candy) / 4)
        else:
            packets = 0

        print(packets)

def solution3():
    nOfTestCases = int(input())
    inputs = []

    for i in range(0, nOfTestCases):
        hours = int(input())
        inputs.append(hours)

    for j in range(0, nOfTestCases):
        if inputs[j] > 10:
            price = 500 + (inputs[j] - 10) * 10
        else:
            price = inputs[j] * 50

        print(price)

def main():
    solution1()
    solution2()
    solution3()

main()
