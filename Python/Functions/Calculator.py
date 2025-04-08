# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")
def add_numbers(a, b):
    print("Adding numbers...")
    return a + b

print("Welcome to the calculator!")
def sub_numbers(a, b):
    print("Subtracting numbers...")
    return a - b

print("Welcome to the calculator!")
def mul_numbers(a, b):
    print("Multiplying numbers...")
    return a * b

print("Welcome to the calculator!")
def div_numbers(a, b):
    print("Dividing numbers...")
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
        
        userAnswer = input("input number")
        userAnswer = float(userAnswer)
        userAnswer2 = input("input second number")
        userAnswer2 = float(userAnswer2)
        result = add_numbers(userAnswer, userAnswer2)
        print(result)
       
    elif userAnswer == "b":
      
        userAnswer = input("input number")
        userAnswer = float(userAnswer)
        userAnswer2 = input("input second number")
        userAnswer2 = float(userAnswer2)
        result = sub_numbers(userAnswer, userAnswer2)
        print(result)

    elif userAnswer == "c":
        
        userAnswer = input("input number")
        userAnswer = float(userAnswer)
        userAnswer2 = input("input second number")
        userAnswer2 = float(userAnswer2)
        result = mul_numbers(userAnswer, userAnswer2)
        print(result)

    elif userAnswer == "d":
        
        userAnswer = input("input number")
        userAnswer = float(userAnswer)
        userAnswer2 = input("input second number")
        userAnswer2 = float(userAnswer2)
        result = div_numbers(userAnswer, userAnswer2)
        print(result)
    
 
    
      

    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")