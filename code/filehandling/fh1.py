# # Writing
# # Flag for writing is w
# f = open("text1.txt", 'w')
# f.write("Hey, suyash!\n")
# f.write("I am alive!\n")
# f.close()

# # Reading
# # Flag for reading is r and that is defaulty set
# f = open("text1.txt")
# print(f.read(3))
# print(f.readline())
# f.close()

# # Appending
# f = open("text1.txt", "a")
# f.write("Heyyy")
# f.close()

# f = open("text1.txt")
# txt = f.readlines()
# for i in txt:
#     print(i)
# f.close()

with open("text1.txt", "a") as f:
    f.write("Nope!\n")