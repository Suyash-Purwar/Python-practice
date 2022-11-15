# Create a class named Student. It must have minimum of two method. 1st getData. 2nd showData

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def getData(self):
        print("Data assigned already")

    def showData(self):
        print("Name: " + str(self.name))
        print("Age: " + str(self.age))
        print("Course: " + str(self.course))

def addTime(time1, time2):
    time1Arr = time1.split(' ')
    time2Arr = time2.split(' ')

    totalSeconds = int(time1Arr[4]) + int(time2Arr[4])
    totalMinutes = int(time1Arr[2]) + int(time2Arr[2])
    totalHours = int(time1Arr[0]) + int(time2Arr[0])

    if (totalSeconds >= 60):
        totalMinutes = totalMinutes + (totalSeconds // 60)
        totalSeconds %= 60
    
    if (totalMinutes >= 60):
        totalHours = totalHours + (totalMinutes // 60)
        totalMinutes %= 60

    return str(totalHours) + " hours " + str(totalMinutes) + " minutes " + str(totalSeconds) + " seconds"

def main():
    stud1 = Student("Ashish Satyam Khan Modi Chaurasia Purwar", 69, "B.Sc")
    print(stud1.name)
    stud1.showData()

    totalTime = addTime("2 hours 50 minutes 50 seconds", "2 hours 100 minutes 100 seconds")
    print(totalTime)

main()
