import pickle as p

file2 = open("dump.txt", "wb")
p.dump(99.6, file2)
p.dump({1, 2, 3}, file2)
p.dump([7, 0, 6], file2)

# Input Data

data1 = {10, 20, 30}
data2 = [50, 60]
data3 = 99
data4 = 70.8

file1 = open("./practical13_data.txt", "w")
for i in data1:
    file1.write(str(i)+", ")
for i in data2:
    file1.write(str(i)+", ")
print(data2)
file1.write(str())
file1.close()