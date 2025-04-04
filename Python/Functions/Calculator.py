# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
def add_numbers(a, b):
    print("Adding numbers...")
    return a + b  # Task 3: Now the function returns the sum of a and b
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
        #ask the user for two numbers
        firstNumber = input("Please enter the first number: ")
        secondNumber = input("Please enter the second number: ")
        firstNumber = float(firstNumber)
        secondNumber = float(secondNumber)

        add_numbers(12,1)
        #call the add_numbers function and print the result
        print("hi!")
    
    elif userAnswer == "b":
        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "d":
        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")