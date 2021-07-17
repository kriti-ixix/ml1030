#User defined functions

'''
Four types of functions:
Parameters: 
- Default function
- Parameterised function

Return types:
- No return type 
- Return type 
'''

def addNumbers():
    print("Addition:")
    x = int(input())
    y = int(input()) 

    print(x + y)


def subNumbers():
    print("Subtraction:")
    x = int(input())
    y = int(input())

    print(x - y)


def multiplyNumbers(x, y):
    print(x*y)


def divideNumbers(x, y):
    return x/y


addNumbers()
subNumbers()
multiplyNumbers(5, 10)
answer = divideNumbers(100, 50)

print("The quotient is", answer)