# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.print

print("")
print("Welcome to the calculator!")
print("")

import random
joke_pairs = [
    ("What do you call a sad strawberry?", "A blueberry!"),
    ("Why did the math book look sad?", "Because it had too many problems!"),
    ("Why was the obtuse angle so sad?", "Because it was never quite right!"),
    ("Why did the student wear glasses in math class?", "To improve di-vision!"),
    ("What is an astronaut's favorite control on the computer keyboard?", "The space bar!"),
    ("Why was the math teacher suspicious of prime numbers?", "Because they were acting odd!"),
    ("Why was the math book so good at making friends?", "Because it had all the right angles!"),
    ("What happened when a dragon breathed on several Macintosh computers?", "It wound up with baked Apples!"),
    ("Why did the student eat their math homework?", "Because their teacher said it was a piece of cake!"),
    ("Why did the chicken cross the Web?","To get to the other site."),
    ("Why souldent you trust adems?", "Because they make up everything!"),
    ("Did you know deer can jump higher than the average house?", "It's because of their strong hind legs and the fact that the average house can't jump."),
    ("Why did the math teacher break up with the calculator?", "Because she felt like she was just a number!"),
    ("Why did the math teacher go to the beach?", "Because she wanted to work on her tan-gent!"),   
    ("Why was the calculator arested?", "Because its story didn't add up!"),
]

def add_numbers(a, b):
    addition = a + b
    return addition

def sub_numbers(a,b):
    subtraction = a - b
    return subtraction

def times_numbers(a,b):
    multiplication = a * b
    return multiplication

def dive_numbers(a,b):
    if b == 0:
        return "Deviding by 0 is NOT nice. Try again. Hmf!"
    divide = a / b
    return divide

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
    print("E. Exit")
    print("J. Joke")
    print(" ")
    userAnswer = input()

    if userAnswer == "+":
        print(" ")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        addition = add_numbers(a, b)    
        print(" ")      
        print(f"Your answer is {addition}")
        print(" ")
    elif userAnswer == "-":
        print(" ")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        subtraction = sub_numbers(a, b)
        print(" ")
        print(f"Your answer is {subtraction}") 
        print(" ")
    elif userAnswer == "x":
        print(" ")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        multiplication = times_numbers(a, b)
        print(" ")
        print(f"Your answer is {multiplication}")
        print(" ")
    elif userAnswer == "/":
        print(" ")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        divide = dive_numbers(a, b)
        if divide == "Deviding by 0 is NOT nice. Try again. Hmf!":
            print(" ")
            print(divide)
            print(" ")
        else:
            print(" ")
            print(f"Your answer is {divide}")
            print(" ")
    elif userAnswer.lower() == "j":
        print(" ")
        question, answer = random.choice(joke_pairs)
        print(question)
        print(" ")
        userAnswer = input("Press Enter to see the answer.")
        print(" ")
        print(answer)
        print(" ")
    elif userAnswer.lower() == "e":
        print(" ")
        print("Thanks for using 'the COOL calculator!'")
        print(" ")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again!")