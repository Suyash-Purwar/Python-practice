# class Calculate:
#     def __init__(self):
#         self.operation = input("Name of the operation: ")
#         self.num = int(input("No of numbers: "))
#         self.numList = []

#         for i in range(0, self.num):
#             self.numList.append(int(input("Enter the number: ")))

#         if self.operation == '+':
#             print(self.summation())
#         elif self.operation == '*':
#             print(self.product())
#         else:
#             print('Mar Jao')

        
#     def summation(self):
#         sum = 0
#         for i in self.numList:
#             sum = sum + i

#         return sum
    
#     def product(self):
#         prod = 1
#         for i in self.numList:
#             prod = prod * i

#         return prod

# result = Calculate()

class A:
    def show(self):
        print("I'm super class")

class A (B):
    def show(self):
        print("I'm child class")

a = A()
a.show()