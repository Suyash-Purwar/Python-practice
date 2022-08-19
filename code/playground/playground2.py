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
        
for i in range(0, len(listOfWords)):
    if wordCount.get(listOfWords[i]) == None:
        wordCount[listOfWords[i]] = 1
    
    for next_words in listOfWords[i+1:len(listOfWords)]:
        if listOfWords[i] == next_words:
            wordCount[listOfWords[i]] = wordCount[listOfWords[i]] + 1

print(wordCount)
