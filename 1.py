class Student(object):
    def __init__(self,name,age,gender,grade):
        self.name=name
        self.age=age
        self.gender=gender
        self.grade=grade
    def printName(self):
        print(self.name)
    def printAge(self):
        print(self.age)
    def setGender(self,gender):
        self.gender=gender
        print(self.gender)

Ali=Student("Ali",13,"male",8)
Ali.printName()
Ali.printAge()
Ali.setGender("M")