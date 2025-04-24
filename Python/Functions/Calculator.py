# Simple text-based calculator

print("Welcome to the calculator!")

# Task 1: Addition function
def add(x, y):
    return x + y

# Task 2: Subtraction function
def subtract(x, y):
    return x - y

# Task 3: Multiplication function
def multiply(x, y):
    return x * y

# Task 4: Division function
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

playing = True
while playing:
    print("Please choose an operation:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    print("e. Exit")
    userAnswer = input()

    if userAnswer == "a":
        # Addition
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result is: {add(num1, num2)}")
    elif userAnswer == "b":
        # Subtraction
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result is: {subtract(num1, num2)}")
    elif userAnswer == "c":
        # Multiplication
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result is: {multiply(num1, num2)}")
    elif userAnswer == "d":
        # Division
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result is: {divide(num1, num2)}")
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")