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
        userAnswer = input("Please enter two numbers separated by a space: ")
        numbers = userAnswer.split()
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        add_numbers = lambda x, y: x + y
        result = add_numbers(num1, num2)
        print(f"The result of adding {num1} and {num2} is: {result}")
    elif userAnswer == "b":
        # Replace pass with getting user input and calling your function
        userAnswer = input("Please enter two numbers separated by a space: ")
        numbers = userAnswer.split()    
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        subract_numbers = lambda x, y: x - y
        result = subtract_numbers(num1, num2)
        print(f"The result of subtracting {num1} from {num2} is: {result}")
    elif userAnswer == "c":
        # Replace pass with getting user input and calling your function
        userAnswer = input("Please enter two numbers separated by a space: ")
        numbers = userAnswer.split()
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        multiply_numbers = lambda x, y: x * y
        result = multiply_numbers(num1, num2)
        print(f"The result of multiplying {num1} and {num2} is: {result}")
    elif userAnswer == "d":
        # Replace pass with getting user input and calling your function
        userAnswer = input("Please enter two numbers separated by a space: ")
        numbers = userAnswer.split()
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            divide_numbers = lambda x, y: x / y
            result = divide_numbers(num1, num2)
            print(f"The result of dividing {num1} by {num2} is: {result}")

    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")