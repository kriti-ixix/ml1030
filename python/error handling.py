try:
    myList = [1, 2, 3]
    print(myList[0]) #IndexError

    myDict = {'a':1, 'b':2, 'c':3, 'd':4, 'f':[10, 20, 30, 40]}
    print(myDict['z']) #KeyError

except IndexError:
    print("Index does not exist")

except KeyError:
    print("Key does not exist")

except Exception as e:
    print(str(e))

finally:
    print("End of program")