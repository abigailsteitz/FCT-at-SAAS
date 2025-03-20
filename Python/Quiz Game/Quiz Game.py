# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch.
print("Hello World")
print("Welcome to my trivia")
score = 0

# Question 1
print("Q1: What is the largest desert in the world?")
print("a) Antarctic Desert")
print("b) Sahara Desert")

userAnswer = input("Enter your answer (a/b): ").strip().lower()

if userAnswer == "a": 
    print("CORRECT")
    score += 1
elif userAnswer == "b": 
    print("WRONG")
else: 
    print("???")

# Question 2
print("Q2: What is the only planet in our solar system that rotates on its side?")
print("a) Uranus")
print("b) Neptune")

userAnswer = input("Enter your answer (a/b): ").strip().lower()

if userAnswer == "a": 
    print("CORRECT")
    score += 1
elif userAnswer == "b": 
    print("WRONG")
else: 
    print("???")

# Question 3
print("Q3: What is the hardest natural substance on Earth?")
print("a) Gold")
print("b) Diamond")

userAnswer = input("Enter your answer (a/b): ").strip().lower()

if userAnswer == "b": 
    print("CORRECT")
    score += 1
elif userAnswer == "a": 
    print("WRONG")
else: 
    print("???")

# Question 4
print("Q4: What is the capital of Japan?")
print("a) Kyoto")
print("b) Tokyo")

userAnswer = input("Enter your answer (a/b): ").strip().lower()

if userAnswer == "b": 
    print("CORRECT")
    score += 1
elif userAnswer == "a": 
    print("WRONG")
else: 
    print("???")

# Question 5
print("Q5: What is the smallest bone in the human body?")
print("a) Femur")
print("b) Stapes (in the ear)")

userAnswer = input("Enter your answer (a/b): ").strip().lower()

if userAnswer == "b": 
    print("CORRECT")
    score += 1
elif userAnswer == "a": 
    print("WRONG")
else: 
    print("???")

# Final Score
print("Your final score is: " + str(score) + "/5")
print ("Thanks for playing :)")