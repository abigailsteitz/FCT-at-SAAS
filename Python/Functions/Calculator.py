# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
# TODO: Task 2, same but subtraction
# TODO: Task 3, same but multiplication
# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
def add_numbers(a, b):
    return a + b

# TODO: Task 2, same but subtraction
def subtract_numbers(a, b):
    return a - b

# TODO: Task 3, same but multiplication
def multiply_numbers(a, b):
    return a * b

# TODO: Task 4, same but division
def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

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
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result is: {add_numbers(num1, num2)}")
    elif userAnswer == "b":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result is: {subtract_numbers(num1, num2)}")
    elif userAnswer == "c":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result is: {multiply_numbers(num1, num2)}")
    elif userAnswer == "d":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The result is: {divide_numbers(num1, num2)}")
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")