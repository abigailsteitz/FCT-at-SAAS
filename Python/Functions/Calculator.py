# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
# Define the add_numbers function
def add_numbers(a, b):
    return a + b
# TODO: Task 2, same but subtraction
def subtract_numbers(a, b):
    return a - b
# TODO: Task 3, same but multiplication
def multipfly_numbers(a, b):
    return a * b
# TODO: Task 4, same but division
def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
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
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        
        num1 = float(num1) 
        num2 = float(num2)

        result = add_numbers(num1, num2)
        print('The result is: ', result)

    if userAnswer == "b":
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        num1 = float(num1) 
        num2 = float(num2)

        result = subtract_numbers(num1, num2)
        print('The result is: ', result)

    elif userAnswer == "c":
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        num1 = float(num1) 
        num2 = float(num2)

        result = multipfly_numbers(num1, num2)
        print('The result is: ', result)

    elif userAnswer == "d":
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        num1 = float(num1) 
        num2 = float(num2)

        result = divide_numbers(num1, num2)
        print('The result is: ', result)


        
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")
