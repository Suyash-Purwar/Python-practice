sentence = "Suyash is mad. Suyash is idiot"
tempStr = ""
listOfWords = []
wordCount = {}
for i in range(0, len(sentence)):
    if sentence[i] != " ":
        tempStr = tempStr + sentence[i]
    else:
        listOfWords.append(tempStr)
        tempStr = ""


for word in listOfWords:
    if wordCount.get(word) == None:
        wordCount[word] = 1

    listOfWords.remove(word)
    for next_words in listOfWords:
        if word == next_words:
            wordCount[word] = wordCount[word] + 1
        
print(wordCount)

# dict1 = {
#     "name": "Suyash"
# }

# print(dict1.get("name2") == None)