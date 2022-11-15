import random
import pickle as p

file = open("dump2.txt", "w")
for i in range(0, 10):
    x = random.randint(50, 100)
    file.write(str(x)+", ")
file.close()

f = open("./dump3.txt", "w")
f.write("Delete all H and i when both are together")
f.write("\nHello Hi PythonHiCSE Hi Hello Hi")
f.close()

f = open("./dump3.txt", "r")
f1 = f.read()
d = f1.replace("Hi", "")
print(d)
