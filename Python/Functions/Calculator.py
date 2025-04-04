# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")

# TODO: Task 1, write a function that takes two numbers as parameters and returns their sum.
def add_numbers(a, b):
        return a + b
def subtract_numbers(a, b):
        return a - b
def multiply_numbers(a, b):
        return a * b
def divide_numbers(a, b):
        return a / b
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
        print("what numbers would you like to add")

    
    
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"the result is: {add_numbers(num1, num2)}")





    if userAnswer == "b":
        print("what numbers would you like to subtract")
    
    
    
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"the result is: {subtract_numbers(num1, num2)}")


    if userAnswer == "c":
        print("what numbers would you like to multiply")
    
    
    
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"the result is: {multiply_numbers(num1, num2)}")



    if userAnswer == "d":
        print("what numbers would you like to divide")
    
 
    
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"the result is:{divide_numbers(num1, num2)}")


    if userAnswer == "e":
        print("thank you for using the calculator")
        playing = False
        
    else:
        print("please enter a valid operation")
        playing = True
     
       
       
        
   