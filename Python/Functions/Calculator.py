# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
# TODO: Task 2, same but subtraction
# TODO: Task 3, same but multiplication
# TODO: Task 4, same but division

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero!"
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
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = add_numbers(a, b)
        print(f"The result of adding {a} and {b} is: {result}")
    elif userAnswer == "b":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = subtract_numbers(a, b)
        print(f"The result of subtracting {b} from {a} is: {result}")
    elif userAnswer == "c":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = multiply_numbers(a, b)
        print(f"The result of multiplying {a} and {b} is: {result}")
    elif userAnswer == "d":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = divide_numbers(a, b)
        print(f"The result of dividing {a} by {b} is: {result}")
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")