# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
def add_numbers(a, b):
    print("Adding numbers...")
    return a + b
# TODO: Task 2, same but subtraction
def subtract_numbers(a, b):
    print("Substracting...")
    return a - b
# TODO: Task 3, same but multiplication
def multiply_numbers(a, b):
    print("Multiplying...")
    return a * b
# TODO: Task 4, same but division
def divide_numbers(a, b):
    print("dividing...")
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
        #get user input
        print("give me number")
        userAnswer = input()
        userAnswer = float(userAnswer)
        print("give me number")
        userAnswer2 = input()
        userAnswer2 = float(userAnswer2)
        #make sure they are numbers
        #call your function
        result=add_numbers(userAnswer,userAnswer2)
        #print the result
        print(result)
        pass
    elif userAnswer == "b":
         # Replace pass with getting user input and calling your function
        #get user input
        print("give me number")
        userAnswer = input()
        userAnswer = float(userAnswer)
        print("give me number")
        userAnswer2 = input()
        userAnswer2 = float(userAnswer2)
        #make sure they are numbers
        #call your function
        result=subtract_numbers(userAnswer,userAnswer2)
        #print the result
        print(result)
        pass
    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function'
        print("give me number")
        userAnswer = input()
        userAnswer = float(userAnswer)
        print("give me number")
        userAnswer2 = input()
        userAnswer2 = float(userAnswer2)
        #make sure they are numbers
        #call your function
        result=multiply_numbers(userAnswer,userAnswer2)
        #print the result
        print(result)
        pass
    elif userAnswer == "d":
        print("give me number")
        userAnswer = input()
        userAnswer = float(userAnswer)
        print("give me number")
        userAnswer2 = input()
        userAnswer2 = float(userAnswer2)
        #make sure they are numbers
        #call your function
        result=divide_numbers(userAnswer,userAnswer2)
        #print the result
        print(result)
        # Replace pass with getting user input and calling your function
        pass
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")