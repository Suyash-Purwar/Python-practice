list1 = [4, 3, -3, 0, 7, 4, 2, 6]
print(list1[2:4]) # -3, 0
print(list1[::-1]) # Reversed

print(type(range(10)))
list2 = list(range(10))
print(list2)

list3 = list(range(5, 50, 2)) # 5 -> 49
print(list3)

# Run backwards with the step 2
list4 = list(range(10, 0, -2))
print(list4)
# 2nd element from the backwards
print(list4[-2])

list5 = ["Suyash", "Shubham", "Anshuman", "Sandeep", "Nikhil"]
print("Nikhil" in list5) # True
print("Anshuman" not in list5) # False

# Creates 3 copies
print(list1*3)

# Concatenate arrays
print(list5+list2)

# Two arrays are equals if all the elements are identical

# Elements from the 2nd index to 4th index are removed and three elements are inserted
list5[2:4] = ["Mummy", "Papa", "Rashi"]
print(list5)

# Deletes all the messages from the 4th element
del list5[4:]
print(list5)

# Shallow copies the array
list5_copy = list5
print(id(list5_copy), id(list5)) # ID's are same

# Deep copies the array
list5_copy = list5[:]
print(id(list5_copy), id(list5)) # ID's are different

str1 = "My name is Suyash"
str1_split = str1.split(" ")
str1_updated = "_".join(str1_split)
print(str1_updated)
print("".join(str1_split)) # MynameisSuyash

list6 = ["1", "2", "3", "4"]
print(", ".join(list6))

# Two arrays can be merged like this as well
merged_arr = [*list6, *list5_copy]
print(merged_arr)
print(list6 + list5_copy)

print(list2)
print(sum(list2))
print(min(list2))
print(max(list2))
list2.append(9)
print(list2.count(9))
list2.reverse()
print(list2)
