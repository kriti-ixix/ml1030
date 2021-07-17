try:
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))

    if length < 0 or breadth < 0:
        raise ValueError

    print("The area is", length*breadth)

except ValueError:
    print("The values cannot be negative")

except Exception as e:
    print(str(e))