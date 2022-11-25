import re

# Character Sets/Classes
# The character sets/classes allows us to define a character that will match if any of the defined characters on the set is preset
# Example 1: Suppose if we want to find all the occurences of license and licence in the text

txt1 = "Yesterday, I was driving my car without a driving licence. The traffic police stopped me and asked me for my license. I told them that I forgot my licence at home."

txt2 = "The first season of Indian Premiere League (IPL) was played in 2008. The second season was played in 2009 in South Africa. Last season was played in 2018 and won by Chennai Super Kings (CSK). CSK won the title in 2010 and 2011 as well. Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017."

txt3 = "Some random text.\nI just want to say that I have so much work to do.\nDeadlines are approaching.\nBrain do your thing well ffs!.\n"

# Solution of Example 1
ptrn1 = re.compile("licen[cs]e")
match1 = ptrn1.findall(txt1)
print(match1)

# Find all the years
ptrn2 = re.compile("[1-9][0-9][0-9][0-9]")
match2 = ptrn2.findall(txt2)
print(match2)

# Find all the consonants
# ^ -> Inverts the condition
ptrn3 = re.compile("[^aeiou ]")
match3 = ptrn3.findall(txt1)
print(match3)

# Find all the capital letters
ptrn4 = re.compile("[A-Z]")
match4 = ptrn4.findall(txt2)
print(match4)

# Find all characters except the new line character
ptrn5 = re.compile(".")
match5 = ptrn5.findall(txt3)
print(match5)

# Find all the new line characters
match6 = re.findall(r"\n", txt3)
print(match6)

# . 	This element matches any character except newline
# \d 	This matches any decimal digit; this is equivalent to the class [0-9]
# \D 	This matches any non-digit character; this is equivalent to the class [^0-9]
# \s 	This matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v]
# \S 	This matches any non-whitespace character; this is equivalent to the class[^\t\n\r\f\v]
# \w 	This matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_]
# \W 	This matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_]

# Find all the special characters
match7 = re.findall("[^\w\s]", txt2)
print(match7)

# Find all the whitespace characters
match8 = re.findall(" ", txt3)
print(match8)