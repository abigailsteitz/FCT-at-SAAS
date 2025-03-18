print("Hello World")

print("Welcome to the quiz on Stuff and Things")

# Initialize score
score = 0

#this is a variable
userAnswer = input("What is the capital of Washington State? ")
print(userAnswer)

#this is a conditional
if userAnswer.strip().lower() == "olympia":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

userAnswer = input("How many legs does a spider have? ")
print(userAnswer)
if userAnswer.strip() == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

userAnswer = input("What is 5 + 7? ")
print(userAnswer)
if userAnswer.strip() == "12":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

userAnswer = input("What is the chemical symbol for water? ")
print(userAnswer)
if userAnswer.strip().lower() == "h2o":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

userAnswer = input("Who wrote 'To Kill a Mockingbird'? ")
print(userAnswer)
if userAnswer.strip().lower() == "harper lee":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Quiz complete! Your final score is " + str(score) + " out of 5. Thanks for playing!")