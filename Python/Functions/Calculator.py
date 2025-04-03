# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

def add_numbers(num1, num2):
    return float(num1) + float(num2) 


# Function to subtract two numbers
def subtract_numbers(num1, num2):
    return float(num1) - float(num2) 

# Function to multiply two numbers
def multiply_numbers(num1, num2):
    return float(num1) * float(num2) 

# Function to divide two numbers
def divide_numbers(num1, num2):
    try:
        num2 = float(num2)
    except ValueError:
        return "Invalid input! Please enter a valid number."
    if num2 == 0:  # Check for division by zero
        return "Cannot divide by zero!"
    return float(num1) / float(num2)  

while True:
    print("Please choose an operation:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    print("e. Exit")
    user_choice = input()
    if user_choice == "a":
        print("You chose addition!")
        try:
            print("Please enter the first number:")
            firstNum = float(input())
            print("Please enter the second number:")
            secondNum = float(input())
            print("The result is:")
            print(add_numbers(firstNum, secondNum))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
    
    elif user_choice == "b":
        print("You chose subtraction!")
        try:
            print("Please enter the first number:")
            firstNum = float(input())
            print("Please enter the second number:")
            secondNum = float(input())
            print("The result is:")
            print(subtract_numbers(firstNum, secondNum))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")



    elif user_choice == "c":
        print("You chose multiplication!")
        print("Please enter the first number:")
        firstNum = float(input())
        print("Please enter the second number:")
        secondNum = float(input())
        print("The result is:")
        print(multiply_numbers(firstNum, secondNum))

    elif user_choice == "d":
        print("You chose division!")
        print("Please enter the first number:")
        firstNum = float(input())
        print("Please enter the second number:")
        secondNum = float(input())
        print("The result is:")
        print(divide_numbers(firstNum, secondNum))
        
    
    elif user_choice == "e":
        print("Thanks for using the calculator!")
        break
        playing = False

    else:
        print(f"Invalid choice. Please select a valid option.")