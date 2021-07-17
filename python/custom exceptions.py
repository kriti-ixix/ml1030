class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass 

guess = 10

while True:
    try:
        userInput = int(input("Enter your guess: "))

        if userInput > guess:
            raise ValueTooLargeError
        elif userInput < guess:
            raise ValueTooSmallError
        else:
            print("You guessed correctly")
            break

    except ValueTooSmallError:
        print("Guess was too small")

    except ValueTooLargeError:
        print("Guess was too large")

    except:
        print("Error")