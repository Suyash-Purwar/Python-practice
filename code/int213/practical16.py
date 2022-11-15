file = open("something.txt", "r")
vowels = ["a", "e", "i", "o", "u"]
vowels_count = 0
alphabet_count = 0
constants_count = 0
for i in range(3):
    data = file.readline()
    for i in data:
        alphabet_count+=1
        if (i.lower() in vowels):
            vowels_count+=1
        else:
            constants_count+=1

print("Vowels Count: ", vowels_count)
print("Consonants Count: ", constants_count)
print("Alphabet Count: ", alphabet_count)