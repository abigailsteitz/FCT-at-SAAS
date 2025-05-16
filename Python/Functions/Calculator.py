# Interactive Calculator Program. #I used some AI for the things I did not know but I used most code from the first template. But let me explain everything to you. THe program displays a meny with options for additon, subtraction, multicplication, and division. Then the User will input the letter to tell the code which one it wants to use. Then based on the uswrs answer the program acts on the selected opperation. The program will keep running until the user selects the exit option. The program checks for invalid inputs and dispolays error messaging if this is the case with the equation.
a

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def calculator():
    print("Welcome to the Calculator!")
    playing = True

    while playing:
        print("\nPlease choose an operation:")
        print("a. Addition")
        print("b. Subtraction")
        print("c. Multiplication")
        print("d. Division")
        print("e. Exit")
        
        user_choice = input("Enter your choice: ").lower()

        if user_choice in ['a', 'b', 'c', 'd']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if user_choice == 'a':
                    print(f"The result of addition is: {add(num1, num2)}")
                elif user_choice == 'b':
                    print(f"The result of subtraction is: {subtract(num1, num2)}")
                elif user_choice == 'c':
                    print(f"The result of multiplication is: {multiply(num1, num2)}")
                elif user_choice == 'd':
                    print(f"The result of division is: {divide(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif user_choice == 'e':
            print("Thanks for using the calculator! Goodbye!")
            playing = False
        else:
            print("Invalid choice. Please try again.")

# Run the calculator
calculator()