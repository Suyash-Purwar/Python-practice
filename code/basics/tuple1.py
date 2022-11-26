# Tuple is immutable
tuple1 = 1, 2, 3, 4, 5, 6
print(tuple1)

tuple2  = ("Suyash",) + tuple1[3:]
print(tuple2)

user = (1, "Suyash", 20, "12100435")
id, name, age, reg_no = user
print(id)
print(name)
print(age)
print(reg_no)

def show_user(*info):
    for i in info:
        print(i)

show_user("Shubham", 25, "Bhai")

list1 = ["Suyash", "Shubham", "Mummy"]
tuple3 = tuple(list1)

print(len(user))

email = "suyash@gmail.com"
name, domain = email.split("@")
print(name, domain)
