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
        # Get two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        # Call the add_numbers function and print the result
        result = add_numbers(num1, num2)  
        print(f"The result is: {result}")

    elif userAnswer == "b":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = subtract_numbers(num1, num2)
        print(f"The result is: {result}")

        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "c":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))        
        result = multiply_numbers(num1, num2)
        print(f"The result is: {result}")

        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "d":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = divide_numbers(num1, num2)
        print(f"The result is: {result}")

        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "e":
        # Exit the program
        print("Exiting the calculator...")
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")