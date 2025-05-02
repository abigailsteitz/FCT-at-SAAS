# Interactive Text-Based Calculator

print("Welcome to the Interactive Calculator!")

# Define functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main loop for the calculator
playing = True
while playing:
    print("\nPlease choose an operation:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    print("e. Exit")
    userAnswer = input("Enter your choice: ").strip().lower()

    if userAnswer in ["a", "b", "c", "d"]:
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if userAnswer == "a":
            print(f"The result is: {add(x, y)}")
        elif userAnswer == "b":
            print(f"The result is: {subtract(x, y)}")
        elif userAnswer == "c":
            print(f"The result is: {multiply(x, y)}")
        elif userAnswer == "d":
            print(f"The result is: {divide(x, y)}")
    elif userAnswer == "e":
        print("Thanks for using the calculator! Goodbye!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")