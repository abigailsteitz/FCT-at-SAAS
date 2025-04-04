# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# Task 1: Function for addition
def add(a, b):
    return a + b

# Task 2: Function for subtraction
def subtract(a, b):
    return a - b

# Task 3: Function for multiplication
def multiply(a, b):
    return a * b

# Task 4: Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

playing = True
while playing:
    print("Please choose an operation:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    print("e. Exit")
    userAnswer = input()

    if userAnswer in ["a", "b", "c", "d"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if userAnswer == "a":
            print(f"The result is: {add(num1, num2)}")
        elif userAnswer == "b":
            print(f"The result is: {subtract(num1, num2)}")
        elif userAnswer == "c":
            print(f"The result is: {multiply(num1, num2)}")
        elif userAnswer == "d":
            print(f"The result is: {divide(num1, num2)}")
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")