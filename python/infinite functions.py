def addNumbers(*values):
    answer = 0

    for x in values:
        answer += x
        print(answer)

addNumbers(5, 10, 15, 20)
addNumbers(5, 10, 200, 463, 432, 93832)