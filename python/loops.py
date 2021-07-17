#For Loop
#While Loop

#1. Iterator 2. Condition 3. Increment/Decrement

i = 1

while i < 11:
    print(i)
    i += 1
else:
    print("You are now done with the loop!")

for i in range(1,11,2):
    print(i)

myList = [1, 2, 3, 4, 5, 6]

for element in myList:
    if element%2 != 0:
        print(element)

for i in range(0,10):
    print(i)
else:
    print("You are now done with the loop")