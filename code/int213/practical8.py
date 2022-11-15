class employee:
    def __init__(self, n, s, a):
        self.name = n
        self.salary = s
        self.__age = a
        print(self)

    def disp(self):
        print(self.name)
        print("Name=", self.name)
        print("Salary=", self.salary)
        print("Age=", self.__age)


emp1 = employee("Habibi Cat", 1000000000, 69)

print(emp1)