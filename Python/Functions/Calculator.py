# Here you will write a simple text based calculator.
# You will write 4 functions, one for each of the 4 basic operations: addition, subtraction, multiplication, and division.

print("Welcome to the calculator!")


def add_Numbers(number1, number2):
            return number1 + number2

def sub_Numbers(number3, number4):
            return number3 - number4

def mul_Numbers(number5, number6):
            return number5 * number6

def div_Numbers(number7, number8):
            return number7 / number8

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
        print("you chose addition!!")
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        total = add_Numbers(number1, number2)
        print(f"The result of addition is: {total}")

    elif userAnswer == "b":
        print("you chose subtraction!!")
        number3 = float(input("Enter the first number: "))
        number4 = float(input("Enter the second number: "))
        total2 = sub_Numbers(number3, number4)
        print(f"The result of addition is: {total2}")
        
    elif userAnswer == "c":
        print("you chose multiplication!!")
        number5 = float(input("Enter the first number: "))
        number6 = float(input("Enter the second number: "))
        total3 = mul_Numbers(number5, number6)
        print(f"The result of addition is: {total3}")

    elif userAnswer == "d":
        print("you chose division!!")
        number7 = float(input("Enter the first number: "))
        number8 = float(input("Enter the second number: "))
        total4 = div_Numbers(number7, number8)
        print(f"The result of addition is: {total4}")
        
    elif userAnswer == "e":
        print("Thanks for using the calculator!")
        playing = False
    else:
        print(f"Invalid input: {userAnswer}. Please try again.")