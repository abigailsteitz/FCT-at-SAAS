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
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    else:
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
        #ask the user for two numbers
        print("Please enter the first number:")
        firstNumber = input()
        print("Please enter the second number:")
        secondNumber = input()
        
        #turn the input into numbers
        firstNumber = float(firstNumber)
        secondNumber = float(secondNumber)
        #call the function and print the result

        result = add_numbers(firstNumber, secondNumber)
        print(f"The result is: {result}")
        
        pass
    elif userAnswer == "b":
        #ask the user for two numbers
        print("Please enter the first number:")
        firstNumber = input()
        print("Please enter the second number:")
        secondNumber = input()

        #turn the input into numbers
        firstNumber = float(firstNumber)
        secondNumber = float(secondNumber)
        #call the function and print the result
        result = subtract_numbers(firstNumber, secondNumber)
        print(f"The result is: {result}")
        pass

    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        #ask the user for two numbers
        print("Please enter the first number:")
        firstNumber = input()
        print("Please enter the second number:")
        secondNumber = input()

        #turn the input into numbers
        firstNumber = float(firstNumber)
        secondNumber = float(secondNumber)
        #call the function and print the result
        result = multiply_numbers(firstNumber, secondNumber)
        print(f"The result is: {result}")
        pass

    elif userAnswer == "d":
        # Replace pass with getting user input and calling your function
        #ask the user for two numbers
        print("Please enter the first number:")
        firstNumber = input()
        print("Please enter the second number:")
        secondNumber = input()

        firstNumber = float(firstNumber)
        secondNumber = float(secondNumber)
        #call the function and print the result
        result = divide_numbers(firstNumber, secondNumber)
        print(f"The result is: {result}")
        pass
        
        pass
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")