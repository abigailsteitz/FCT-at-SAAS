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
        useranswer = input ("Enter two numbers separated by a space: ")
        numbers = useranswer.split()
        number1 = float(numbers[0])
        number2 = float(numbers[1])
        result = add_numbers(number1, number2)
        print(result)

    elif userAnswer == "b":
    # Replace pass with getting user input and calling your function
        useranswer = input ("Enter two numbers separated by a space: ")
        numbers = useranswer.split()
        number1 = float(numbers[0])
        number2 = float(numbers[1])
        result = subtract_numbers(number1, number2)
        print(result)

    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        useranswer = input ("Enter two numbers separated by a space: ")
        numbers = useranswer.split()
        number1 = float(numbers[0])
        number2 = float(numbers[1])
        result = multiply_numbers(number1, number2)
        print(result)
    elif userAnswer == "d":
        # Replace pass with getting user input and calling your function
        useranswer = input ("Enter two numbers separated by a space: ")
        numbers = useranswer.split()
        number1 = float(numbers[0])
        number2 = float(numbers[1])
        result = divide_numbers(number1, number2)
        print(result)

    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")
