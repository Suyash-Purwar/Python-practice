import re

# re.match(string[, pos[, endpos]]) matches the string from 0 index by default
ptrn1 = re.compile("suyash")
match1 = ptrn1.match("suyash, his name is suyash")
match2 = ptrn1.match("I'm suyash", pos=4)

print(match1) # None if the match is not found. Otherwise object
print(match2) 
print(match2.group()) # Returns the matched string
print(match2.span()) # Returns the range in which the match is found

# re.search(string[, pos[, endpos]]) finds the pattern in the whole string
# pos and endpos specify the range within which you want to search
# A flag is passed here which ignores difference in character casing
ptrn2 = re.compile("google", re.IGNORECASE)
match3 = ptrn2.search("I am learning Google Cloud")
# It will start searching from the 6th index. So, it find the latter 'Google'
match4 = ptrn2.search("Google is helping me learn Google Cloud", pos=6)
print(match3)
print(match4)

# re.findall(string[, pos[, endpos]]) returns a list of matches found within the range of pos and endpos
match5 = ptrn2.findall("Google is helping me learn Google Cloud")
print(match5)

# re.finditer(string[, pos[, endpos]]) returns an iterator containing the match object within the range of pos and endpos
match6 = ptrn2.finditer("Google is helping me learn google cloud. Google cloud is developed by google")
print(match6)
print(next(match6)) # prints the first match
for match_obj in match6:
    print(match_obj) # prints the rest of match objects
# All the values of the iterator are exhausted now. Calling the next() on match6 again would throw an error
# print(next(match6))

# Module Level Functions
ptrn3 = re.compile("hehe")
match7 = ptrn3.findall("hehe is evil. hehe is damned. hehe is an emotion")
# Above two statements could be shortened to
match8 = re.findall("hehe", "hehe is evil. hehe is damned. hehe is an emotion")
print(match8)
# But this doesn't allow reusability of the pattern

# Metacharacters needs to be escaped
# This wouldn't work as $ is a metacharacter
# It needs to be escaped (\)
match9 = re.search("$15", "Cost of this t-shirt is $15") # Returns None
print(match9)
match10 = re.search("\$15", "Cost of this t-shirt is $15") # Returns the match object
print(match10)

# If you want to use backslash as a literal, it needs to be escaped with another backslash because backslash is a metacharacter

# In Regular Expressions, there are 11 metacharacters
# 1. Backslash \
# 2. Dollar sign $
# 3. Carret ^
# 4. Dot .
# 5. Pipe Symbol |
# 6. Question Mark ?
# 7. Asterisk *
# 8. Plus sign +
# 9. Paranthesis (, )
# 10. Square bracket [, ]
# 11. Curly bracket {, }