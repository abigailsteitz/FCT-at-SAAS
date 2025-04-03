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
        return "Error: Division by zero is not allowed."
    return a / b

playing = True
while playing:

    print("Please choose an operation a,b,c,d :")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    print("e. Exit")
    userAnswer = input()

    if userAnswer == "a":
        print("You chose addition.")
        print("Please enter two numbers to add.")
        float1 = float(input("Enter first number: "))
        float2 = float(input("Enter second number: "))
        result = add_numbers(float1, float2)
        print(f"The result is: {result}")
        
    elif userAnswer == "b":
        print("You chose subtraction.")
        print("Please enter two numbers to subtract.")
        float1 = float(input("Enter first number: "))
        float2 = float(input("Enter second number: "))
        result = subtract_numbers(float1, float2)
        print(f"The result is: {result}")
        
    elif userAnswer == "c":
        print("You chose multiplication.")
        print("Please enter two numbers to multiply.")
        float1 = float(input("Enter first number: "))
        float2 = float(input("Enter second number: "))
        result = multiply_numbers(float1, float2)
        print(f"The result is: {result}")
        
    elif userAnswer == "d":
        print("You chose division.")
        print("Please enter two numbers to divide.")
        float1 = float(input("Enter first number: "))
        float2 = float(input("Enter second number: "))
        result = divide_numbers(float1, float2)
        print(f"The result is: {result}")
        
    elif userAnswer == "e":
        print("You chose to exit the calculator.")
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")