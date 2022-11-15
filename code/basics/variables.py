name = "Krish"
print(name);
print(type(name));

age = 19
print(name + "'s age is " + str(age));
print(type(age))

yes = True
sentence = "Is " + name + " an adult: " + str(yes)
print(type(yes))

height = 177.67
print("His height is " + str(height) + "cm")
print(type(height))

carName, carColor = "Honda Civic", "Baby Pink"
print(carName, carColor)

ageOfSuyash = ageOfNikhil = ageOfKrish = 19
arrayOfAges = [ageOfSuyash, ageOfKrish, ageOfNikhil];
for age in arrayOfAges:
    print(age, end=" ")