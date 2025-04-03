# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
def add_numbers(a, b):
    print("Adding numbers...")
    return a + b

def subtract_numbers(a, b):
    print("Subtracting numbers...")
    return a - b

def multiply_numbers(a, b):
    print("Multiplying numbers...")
    return a * b

def divide_numbers(a, b):
    print("Dividing numbers...")
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
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
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = add_numbers(a, b)
        print(f"The result is: {result}")

        pass
    elif userAnswer == "b":
        # Replace pass with getting user input and calling your function
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = subtract_numbers(a, b)
        print(f"The result is: {result}")

        pass
    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = multiply_numbers(a, b)
        print(f"The result is: {result}")

        pass
    elif userAnswer == "d":
        # Replace pass with getting user input and calling your function
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = divide_numbers(a, b)
        if result is not None:
            print(f"The result is: {result}")
            
        pass
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")