class Student:
    def __init__(self, n, r, m=0):
        self.name = n
        self.rollno = r
        self.marks = m
        self.percentage = 0

    def calPercentage(self):
        self.percentage = (self.marks * 100) / 50


student1 = Student("Priya", 10, 32)
student2 = Student("Gaurav", 20)

student1.calPercentage()
#print(student1.percentage)

print(student1.marks)
print(student2.marks)