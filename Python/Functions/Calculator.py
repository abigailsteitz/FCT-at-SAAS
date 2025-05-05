# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
def add_numbers(a, b):
    print("adding numbers...")
    return a + b
# TODO: Task 2, same but subtraction
def subtract_numbers(a, b):
    print("subtracting numbers...")
    return a - b
# TODO: Task 3, same but multiplication
def multiply_numbers(a, b):
    print("multiplying numbers...")
    return a * b
# TODO: Task 4, same but division
def divide_numbers(a, b):
    print("dividing numbers...")
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
        print("which numbers would you like to add? first number:")
        a = input()
        print("great!! what would you like to add to this number?")
        b = input()

        add_total = add_numbers(a, b)
        print(add_total)

        # Replace pass with getting user input and calling your function
        # Tasks: get two numbers from the user. Change them from strings to proper numbers, call your function, print the result
        pass
    elif userAnswer == "b":
        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "d":
        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")