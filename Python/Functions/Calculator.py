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
def divide_number(a, b):
    print("Dividing numbers...")
    result = a/b
    return result

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
        print("Please enter the first number:")
        first_number = input()
        first_number = float(first_number)
        print("Please enter the second number:")
        second_number = input()
        second_number = float(second_number)
      
        result = add_numbers(first_number, second_number)
        print(f"The result of adding {first_number} and {second_number} is: {result}")

    elif userAnswer == "b":
        # Replace pass with getting user input and calling your function
        print("Please enter the first number:")
        first_number = input()
        first_number = float(first_number)
        print("Please enter the second number:")
        second_number = input()
        second_number = float(second_number)    
        
        result = subtract_numbers(first_number, second_number)
        print(f"The result of subtracting {second_number} from {first_number} is: {result}")

    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        print("Please enter the first number:")
        first_number = input()
        first_number = float(first_number)  
        print("Please enter the second number:")
        second_number = input()
        second_number = float(second_number)
        
        result = multiply_numbers(first_number, second_number)
        print(f"The result of multiplying {first_number} and {second_number} is: {result}")

    elif userAnswer == "d":
        # Replace pass with getting user input and calling your function
        print("Please enter the first number:")
        first_number = input()
        first_number = float(first_number)
        print("Please enter the second number:")
        second_number = input()
        second_number = float(second_number)

        result = divide_number(first_number, second_number)
        print(f"The result of dividing {first_number} by {second_number} is: {result}")
        
        
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")




