# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
def add_numbers(a, b):
    print("Adding numbers...")
    return a + b
# TODO: Task 2, same but subtraction
def subtract_numbers(a, b):
    print("subtracting numbers...")
    return a - b
# TODO: Task 3, same but multiplication
def multiply_numbers(a, b):
    print("multiply numbers...")
    return a* b
# TODO: Task 4, same but division
def division_numbers(a, b):
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
        # Replace pass with getting user input and calling your function
        userAnswer = input("Please enter two numbers separated by a space: ")
        numbers = userAnswer.split()
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        # Replace pass with getting user input and calling your function
        result = add_numbers(num1, num2)
        print(f"The result of adding {num1} and {num2} is: {result}")
    elif userAnswer == "b":
        # Replace pass with getting user input and calling your function
        userAnswer = input("Please enter two numbers separated by a space: ")
        numbers = userAnswer.split()
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        # Replace pass with getting user input and calling your function
        result = subtract_numbers(num1, num2)
        print(f"The result of subtracting {num1} and {num2} is: {result}")
    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        userAnswer = input("Please enter two numbers separated by a space: ")
        numbers = userAnswer.split()
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        # Replace pass with getting user input and calling your function
        result = multiply_numbers(num1, num2)
        print(f"The result of multiplying d{num1} and {num2} is: {result}")
    elif userAnswer == "d":
        userAnswer = input("Please enter two numbers separated by a space: ")
        numbers = userAnswer.split()
        if len(numbers) != 2:
            print("Error: Please enter exactly two numbers separated by a space.")
            continue
        try:
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = division_numbers(num1, num2)
                print(f"The result of dividing {num1} by {num2} is: {result}")
        except ValueError:
            print("Error: Please enter valid numbers.")
    else:
        print("Thanks for using the calculator!")
        playing = False




