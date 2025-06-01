print("Welcome to the calculator!")

# Task 1: Addition
def add(x, y):
    return x + y

# Task 2: Subtraction
def subtract(x, y):
    return x - y

# Task 3: Multiplication
def multiply(x, y):
    return x * y

# Task 4: Division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero."
    return x / y

playing = True
while playing:
    print("\nPlease choose an operation:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    print("e. Exit")
    userAnswer = input()

    if userAnswer == "a":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result:", add(num1, num2))

    elif userAnswer == "b":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result:", subtract(num1, num2))

    elif userAnswer == "c":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result:", multiply(num1, num2))

    elif userAnswer == "d":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result:", divide(num1, num2))

    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False

    else:
        print(f"Invalid input: {userAnswer}. Please try again.")
        
