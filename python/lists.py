'''
myList = [1, 2, 3, "Kriti", 5673.038, True]

print(len(myList))
print(myList[4])
print(myList[1:4]) #list slicing

#Adding an element
myList.append(45)
myList[4] = 50
print(myList)

#Removing an element
myList.pop() #Deletes the last element
myList.pop(0)
myList.remove('xyz')
myList.reverse() / myList[::-1]
myList.clear()
myList.count()
len(myList)
myList.sort()

print(myList)

print(list(range(1,101)))
'''

myList = list(range(1, 11))
#mySquaredList = []

print(myList)

#for x in myList:
#    number = x**2 
#   mySquaredList.append(number)

mySquaredList = [x**2 for x in myList] #List comprehension
#print(mySquaredList)

myNewList = [x**2 for x in myList if x**2%2==0]
#print(myNewList)

print(myList.count(1))
print(len(myList))