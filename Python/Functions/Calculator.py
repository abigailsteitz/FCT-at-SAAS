# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.print

print("")
print("Welcome to the calculator!")
print("")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
# TODO: Task 2, same but subtraction
# TODO: Task 3, same but multiplication
# TODO: Task 4, same but division

playing = True
while playing:
    print("Please choose an operation:")
    print("")
    print("+. Addition")
    print("-. Subtraction")
    print("x. Multiplication")
    print("/. Division")
    print("e. Exit")
    print(" ")
    userAnswer = input(a,b)

    if userAnswer == a + b:
          a = int(input)
          b = int(input)
          def add_numbers(a, b):
             addition = a + b
             return addition
          print(addition)
    elif userAnswer == "-":
        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "x":
        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "/":
        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again!")