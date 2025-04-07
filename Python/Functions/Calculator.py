# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
# TODO: Task 2, same but subtraction
# TODO: Task 3, same but multiplication
# TODO: Task 4, same but division
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
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
    userAnswer = input("  ")

    if userAnswer == "a":
        # Replace pass with getting user input and calling your function
        print("what is the first numbers would you like to add?")
        firstnumber = input("  ")
        firstnumber = float(firstnumber)
        print("what is the second numbers would you like to add?")
        secondnumber = input("  ")
        secondnumber = float(secondnumber)
        print("The Sum is: ", add(firstnumber, secondnumber))
        
    elif userAnswer == "b":
        # Replace pass with getting user input and calling your function
        print("what is the first numbers would you like to subtract?")
        firstnumber = input("  ")
        firstnumber = float(firstnumber)
        print("what is the second numbers would you like to subtract?")
        secondnumber = input("  ")
        secondnumber = float(secondnumber)
        print("The Difference is: ", subtract(firstnumber, secondnumber))
    
    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        print("what is the first numbers would you like to multiply?")
        firstnumber = input("  ")
        firstnumber = float(firstnumber)
        print("what is the second numbers would you like to multiply?")
        secondnumber = input("  ")
        secondnumber = float(secondnumber)
        print("The Product is: ", multiply(firstnumber, secondnumber))
        
    elif userAnswer == "d":
        # Replace pass with getting user input and calling your function
        print("what is the first numbers would you like to divide?")
        firstnumber = input("  ")
        firstnumber = float(firstnumber)
        print("what is the second numbers would you like to divide?")
        secondnumber = input("  ")
        secondnumber = float(secondnumber)
        print("The Quotient is: ", divide(firstnumber, secondnumber))
        
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
    else:
        print("Invalid input: {userAnswer}. Please try again.")