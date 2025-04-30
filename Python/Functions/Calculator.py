# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
# TODO: Task 2, same but subtraction
# TODO: Task 3, same but multiplication
# TODO: Task 4, same but division

# Function for addition
def add_numbers(num1, num2):
    return num1 + num2

# Function for subtraction
def subtract_numbers(num1, num2):
    return num1 - num2

# Function for multiplication
def multiply_numbers(num1, num2):
    return num1 * num2

# Function for division
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

print("Welcome to the calculator!")

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
        userAnswer = input("Enter two numbers separated by a space: ")
        numbers = userAnswer.split()
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        print(add_numbers(num1, num2))

    elif userAnswer == "b":
        userAnswer = input("Enter two numbers separated by a space: ")
        numbers = userAnswer.split()
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        print(subtract_numbers(num1, num2))

    elif userAnswer == "c":
        userAnswer = input("Enter two numbers separated by a space: ")
        numbers = userAnswer.split()
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        print(multiply_numbers(num1, num2))

    elif userAnswer == "d":
        userAnswer = input("Enter two numbers separated by a space: ")
        numbers = userAnswer.split()
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        print(divide_numbers(num1, num2))

    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")