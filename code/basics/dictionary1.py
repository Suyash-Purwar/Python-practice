x = {}
x[1] = "Hello"
x['2'] = "Suyash"
x['3'] = "Python"

print(x)
print(x.keys())
print(x.values())

for key in x.keys():
    print(key)

for value in x.values():
    print(value)

x['apples'] = 342
x['pears'] = 100
print(x)

del x['pears']

print(x)
print(len(x))
print(x.items())

x_copy = x.copy()
print(id(x_copy), id(x))

print(x_copy.pop("3"))
print(x_copy.pop(1))

str1 = "Hello, my name is Suyash"
char_dict = {}
for char in str1:
    # 0 here signifies that if 'char' key is not found, then use the value 0
    char_dict[char] = char_dict.get(char, 0) + 1

print(char_dict)

user = {
    "name": "Suyash",
    "age": 20
}

user_details = {
    "location": "Jalandhar, Punjab",
    "weight": 60
}

user.update(user_details)
print(user)

print("name" in user)
print("phone" in user)