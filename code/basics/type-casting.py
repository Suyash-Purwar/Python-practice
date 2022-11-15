# type casting = convert the data type of one value to another data type

integer1 = 23
float1 = 92.45
str1 = "Hello"
str2 = "56"
bool1 = True
bool2 = False

# Integer type casting
print("Integer type casting:")
print(int(float1))
print(int(str2))
print(int(bool2)) # 0
print(type(int(bool1))) # integer
# print(int(str1)) # Error

# Float type casting
print("\nFloat type casting:")
print(float(integer1))
print(float(False))
print(float(bool1))
# print(float(str1)) # Error

# Boolean type casting
print("\nBoolean type casting:")
print(bool(float1))
print(bool(str2))
print(bool(0.0)) # False
print(bool("")) # False
print(bool(-1)) # True

# String Type Casting
print("\nString type casting:")
print(str(float1))
print(str(bool2))
print(str(str2)*2)

# Application
age = 19
# print("My age is "+age) # Error
print("My age is "+str(age))