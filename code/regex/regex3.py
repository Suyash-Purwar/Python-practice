import re

text1 = "Suyash has started learning Google Cloud. This course is fucking him over but Suyash is determined, not sure for how long though. Google Cloud is a lengthy topic"
ptrn1 = re.compile("Suyash|Google|Cloud")
match1 = ptrn1.findall(text1)
print(match1)

text2 = "Who are you? What is your name? What are you doing here?"
ptrn2 = re.compile("(Who|What)\s(is|are)")
match2 = ptrn2.findall(text2)
print(match2)