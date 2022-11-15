from dataclasses import replace

f = open("./suyash.txt", "w")
f.write("Hey!\n")
f.write("Hi\n")
f.write("Car\n")
f.close()
f = open("./suyash.txt", "r")

g = open("./suyash_new.txt", "w")
data = f.read()
print(data)
g.write(data)
f.close()
g.close()

f = open("./suyash.txt", "a")
f.write("FUCK YOU")
f.close()

f = open("./suyash.txt", "r")
replaced_word = f.read().replace("FUCK YOU", "GO TO HELL")
f.close()
f = open("./suyash.txt", "w")
f.write(replaced_word)
f.close()


import os
print(os.getcwd())