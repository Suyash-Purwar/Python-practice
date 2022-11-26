class User:
    species = "Homosapies"
    def __init__(self, name, age):
        print("User is created")
        self.__name = name
        self.__age = age

    def greet(self):
        return "Hello, {}".format(self.__name)

    def isAdult(self):
        return self.__age >= 18
    
    def setAge(self, age):
        self.__age = age

    def setName(self, name):
        self.__name = name

    def describe(self):
        print("Name: {}".format(self.__name))
        print("Age: {}".format(self.__age))

suyash = User("Suyash", 20)
anshuman = User("Anshuman", 20)

print(suyash.greet())
print(anshuman.__class__.species)

print(suyash.__class__.greet(anshuman))

# Cannot be read directly as it's a private attribute
# print(suyash.__name)

print(User.species)

class UserDetails(User):
    def __init__(self, name, age, weight, height, phone):
        super().__init__(name, age)
        self.__phone = phone
        self.weight = weight
        self.height = height
        print("User Details are saved")

    def describe(self):
        print("Details".center(50, "-"))
        super().describe()
        print("Phone: {}".format(self.__phone))
        print("Weight: {}".format(self.weight))
        print("Height: {}".format(self.height))

sandeep = UserDetails("Sandeep", 21, 55, 5.6, "9834782309")
sandeep.describe()
# Calling parent's class methods
print(sandeep.greet())
print(sandeep.__class__.species)
print(sandeep.isAdult())