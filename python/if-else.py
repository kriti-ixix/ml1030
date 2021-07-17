age = int(input("Enter your age: "))

if age > 17:
    print("You are eligible to vote")
elif age > 15 and age < 18:
    print("You are almost eligible")
elif age < 0:
    print("How is your age negative")
else:
    print("You are not eligible to vote")
