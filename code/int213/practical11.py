class Student:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

    def scream(self):
        print(self.name+self.name[0]*4)

    def scream(self, message):
        print(message+message[0]*6 + " " + self.name)

class Account:
    def __init__(self, id, balance, interest):
        self.__id = id
        self.__balance = balance
        self.__interest = interest

    def getMonthlyInterestRate(self):
        return "Monthly interest rate is " + str((self.__interest/100)/12)
    
    def getBalance(self):
        return "Current balance with an year of interest " + str(self.__balance + (self.__balance * (self.__interest/100/12)))

    def withdraw(self, amount):
        if (self.__balance < amount):
            return "Not possible"
        else:
            self.__balance -= amount
            return str(self.__interest) + " deposited"
    
    def deposit(self, amount):
        self.__balance += amount
        return str(amount) + " deposited"
        

def main():
    student1 = Student("Suyash", 19, ['Photography'])
    student1.scream()

    account1 = Account(12100435, 100, 4)
    print(account1.withdraw(1010))
    print(account1.deposit(1000))
    print(account1.getMonthlyInterestRate())
    print(account1.getBalance())

main()