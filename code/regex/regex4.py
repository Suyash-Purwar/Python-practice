import re

# Symbol 	Name 	        Quantification of previous character
# ? 	    Question Mark 	Optional (0 or 1 repetitions)
# * 	    Asterisk 	    Zero or more times
# + 	    Plus Sign 	    One or more times
# {n,m} 	Curly Braces 	Between n and m times

text1 = "I have 2 dogs. One dog is 1 year old and other one is 2 years old. Both dogs are very cute!"

text2 = """
file1.txt
file_one.txt
file.txt
fil.txt
file.xml
file-1.txt
"""

text3 = """
file1.txt
file_one.txt
file09.txt
fil.txt
file23.xml
file.txt
"""

text4 = "Helloooo Hellooo Helloo Hellooooooo Hello"

text5 = """
The first season of Indian Premiere League (IPL) was played in 2008. 
The second season was played in 2009 in South Africa. 
Last season was played in 2018 and won by Chennai Super Kings (CSK).
CSK won the title in 2010 and 2011 as well.
Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
"""

text6 = """
555-555-5555
555 555 5555
5555555555
666 666-6666
"""

ptrn1 = re.compile("dogs?")
match1 = ptrn1.findall(text1)
print(match1)

ptrn2 = re.compile("file[\w-]*.txt")
match2 = ptrn2.findall(text2)
print(match2)

ptrn3 = re.compile("file\d+.txt")
match3 = ptrn3.findall(text3)
print(match3)

# Syntax 	Description
# {n} 	    The previous character is repeated exactly n times.
# {n,} 	    The previous character is repeated at least n times.
# {,n} 	    The previous character is repeated at most n times.
# {n,m} 	The previous character is repeated between n and m times (both inclusive).

# Find all the Hello's with more than or equal to 2 o's
ptrn4 = re.compile("Hello{3,}")
match4 = ptrn4.findall(text4)
print(match4)

# Find all the years
ptrn5 = re.compile("\d{4}")
match5 = ptrn5.findall(text5)
print(match5)

# Telephone numbers can be of the form: 555-555-5555, 555 555 5555, 5555555555
# But there's a problem
ptrn6 = re.compile("\d{3}[-\s]?\d{3}[-\s]?\d{4}")
match6 = ptrn6.findall(text6)
print(match6)