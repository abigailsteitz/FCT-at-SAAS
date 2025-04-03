# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
# TODO: Task 2, same but subtraction
# TODO: Task 3, same but multiplication
# TODO: Task 4, same but division

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
        # Example:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = (num1 + num2)
        print(f"The result is: {result}")
        
    elif userAnswer == "b":
        # Replace pass with getting user input and calling your function
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = (num1 - num2)
        print(f"The result is: {result}")
        
    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = (num1 * num2)
        print(f"The result is: {result}")
        
    elif userAnswer == "d":
        # Replace pass with getting user input and calling your function
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = (num1 / num2)
        print(f"The result is: {result}")
        
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")