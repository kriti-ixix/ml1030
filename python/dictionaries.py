'''
myDict = {'a':1, 'b':2, 'c':3, 'd':4, 'f':[10, 20, 30, 40]}

for x in myDict:
    print(x)

for x in myDict.items():
    print(x)

for (x, y) in myDict.items(): #Dictionary unpacking
    print("Key:", x, "Value:", y)

myDict['g'] = 7
print(myDict)

myDict['g'] = 10
print(myDict)
'''

myList = list(range(1, 11))
'''
for x in myList:
    myDict[x] =  x**2
'''

myDict = {x:x**2 for x in myList}
print(myDict)