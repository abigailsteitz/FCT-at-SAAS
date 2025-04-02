# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
# TODO: Task 2, same but subtraction
# TODO: Task 3, same but multiplication
# TODO: Task 4, same but division
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b  # Note: This will raise an error if b is 0, which we will handle later
   

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
        firstnumber = input("Give me a first number ")
        secondnumber = input("Give me a second number ")
        # Convert inputs to numbers
        firstnumber = float(firstnumber)
        secondnumber = float(secondnumber)
        # Call the addition function and print the result
        result = addition(firstnumber, secondnumber)  
        print(f"The result is: {result}")
    elif userAnswer == "b":
        # Replace pass with getting user input and calling your function
        firstnumber = input("Give me a first number: ")
        secondnumber = input("Give me a second number: ")
        # Convert inputs to numbers
        firstnumber = float(firstnumber)
        secondnumber = float(secondnumber)
        # Call the subtraction function and print the result
        result = subtraction(firstnumber, secondnumber)
        print(f"The result is: {result}")
    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        firstnumber = input("Give me a first number ")
        secondnumber = input("Give me a second number ")
        # Convert inputs to numbers
        firstnumber = float(firstnumber)
        secondnumber = float(secondnumber)
        # Call the multiplication function and print the result
        result = multiplication(firstnumber, secondnumber)  
        print(f"The result is: {result}")
    elif userAnswer == "d":
        # Replace pass with getting user input and calling your function
        firstnumber = input("Give me a first number ")
        secondnumber = input("Give me a second number ")
        # Convert inputs to numbers
        firstnumber = float(firstnumber)
        secondnumber = float(secondnumber)
        # Call the division function and print the result
        result = division(firstnumber, secondnumber)
        if isinstance(result, str):  # Check if result is an error message
            print(result)
        else:
            print(f"The result is: {result}")
    # Check if the user wants to exit
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")


def get_numbers():
    # Get user input for two numbers and convert to float
    firstnumber = float(input("Give me a first number: "))
    secondnumber = float(input("Give me a second number: "))
    return firstnumber, secondnumber
