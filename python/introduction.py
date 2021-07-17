#name = "Kriti Bhatia"
#roll_no = 10
#marks = 45.5

'''
Four data types:
String -> "My name will be stored here"
Integer -> 5, 10, -1000
Float -> 5.0, 10.57, 0.05649
Boolean -> True/False
'''

name = input("Enter your name: ") #Default input is stored in the string
roll_no = int(input("Enter your roll number: "))
marks = float(input("Enter your marks: "))

'''
print(name)
print(roll_no)
print(marks)
'''

print(type(name), end="! ")
print(type(roll_no), end = "! ")
print(type(marks),end = "! ")