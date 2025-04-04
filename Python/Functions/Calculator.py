# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
def add_numbers(a, b):
    print("Adding numbers...")
    return a + b
# TODO: Task 2, same but subtraction
def subtract_numbers(a, b):
    print("Subtracting numbers...")
    return a - b
# TODO: Task 3, same but multiplication
def multiply_numbers(a, b):
    print("Multiplying numbers...")
    return a * b
# TODO: Task 4, same but division
def divide_numbers(a, b):
    print("Dividing numbers...")
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
        # Replace pass with getting user input and calling your function
        print("You chose addition.")
        print("Please enter the first number:")
        firstNumber = float(input())
        print("Please enter the second number:")
        secondNumber = float(input())
        total = add_numbers(firstNumber, secondNumber) 
        print (total)
    elif userAnswer == "b": 
        # Replace pass with getting user input and calling your function
        print("You chose subtraction.")
        print("Please enter the first number:")
        firstNumber = float(input())
        print("Please enter the second number:")
        secondNumber = float(input())
        total = subtract_numbers(firstNumber, secondNumber) 
        print (total)
    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        print("You chose multiplication.")
        print("Please enter the first number:")
        firstNumber = float(input())
        print("Please enter the second number:")
        secondNumber = float(input())
        total = multiply_numbers(firstNumber, secondNumber) 
        print (total)
    elif userAnswer == "d":
        # Replace pass with getting user input and calling your function
        print("You chose multiplication.")
        print("Please enter the first number:")
        firstNumber = float(input())
        print("Please enter the second number:")
        secondNumber = float(input())
        total = divide_numbers(firstNumber, secondNumber) 
        print (total)
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")