even_no = [i for i in range(1, 51) if i % 2 == 0]
odd_no = [i for i in range(1, 50)  if i % 2 != 0]

# Approach 1
new_list = []
new_list.extend(odd_no)
new_list.extend(odd_no)
new_list.sort()
print(new_list, end="\n\n")

# Approach 2
# Sorted by design
new_list2 = []
for i in range(len(even_no)):
    new_list2.append(odd_no[i])
    new_list2.append(even_no[i])

print(new_list2, end="\n\n")

array = [1, 1, 2, 4, 5, 8, 2]
# Reverses the array
print(array[::-1])

string_num = "1234"
arr_num = [int(i) for i in [*string_num]]
sum = 0
for i in arr_num:
    sum += i

print(sum)