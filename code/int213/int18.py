import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

y = re.search("\s", txt)
print(y.start())