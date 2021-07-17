myDict = {'a':1, 'b':2, 'c':3, 'd':4, 'f':[10, 20, 30, 40]}

file = open("/Users/kritixblaze/Desktop/Dictionary.txt", 'w')

for (x, y) in myDict.items():
    file.write("Key: " + x + " Value: " + str(y) + "\n")

file.close()