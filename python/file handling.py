vacationPlaces = ['New York', 'Paris', 'London', 'Los Angeles']

vacationFile = open("Vacations.txt", 'w')

for vacation in vacationPlaces:
    vacationFile.write(vacation + "\n")

vacationFile.close()

vacationFile = open("Vacations.txt", 'r')

for line in vacationFile:
    print(line)

entireFile = vacationFile.read()
print(entireFile)

vacationFile.close()