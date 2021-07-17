scores = 325
wickets = 7
catch = 4
listOfConditions = [scores>320, wickets<8, catch>3]

if all(listOfConditions):
    print("Winner")


scores = 200
wickets = 7
catch = 4

if any(listOfConditions):
    print("Winner")