def times2(var):
    return var * 2

seq = [1, 2, 3, 4, 5]

print(list(map(times2, seq)))

l = lambda var : var * 2
print(l(10))

print(list(map(lambda var : var * 2, seq)))

print(list(filter(lambda x : x%2 == 0, seq)))

print("Odd" if int(input("Enter a number: "))%2!=0 else "Even")

myList = []

for x in seq:
    myList.append(times2(x))