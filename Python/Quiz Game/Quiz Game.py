# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch.
print("Hello World")
print("Welcome to my quiz about the world")
print("Please input the letter of the answer")
print("Question 1: How many countries are there?")
score = 0
userAnswer = input()
if userAnswer == "195": 
  print("correct")
  score = score + 1 
else:
  print("that's wrong")
print("Question 2: What is the biggest country?")
userAnswer = input()
if userAnswer == "Russia" or userAnswer == "russia":
  print("correct")
  score = score + 1 
else:
  print("that's wrong")
print("Question 3: What country has the highest population?")
userAnswer = input()
if userAnswer == "India" or userAnswer == "india":
  print("correct")
  score = score + 1 
else:
  print("that's wrong")
print("Question 4: What is the name of the largest ocean?")
userAnswer = input()
if userAnswer == "Pacific Ocean" or userAnswer == "pacific ocean":
  print("correct")
  score = score + 1
else:
  print("that's wrong")
print("Question 5: What is the name of the largest desert?")
userAnswer = input()
if userAnswer == "Antartic Polar Desert" or userAnswer == "antartic polar desert" or userAnswer == "Antarctica" or userAnswer == "antartica":
  print("correct")
  score = score + 1
else:
  print("that's wrong")

print("You got" + str(score) + "/5correct!")
  
if score == 5: 
  print("What is the only continent where coffee grows naturally?")
userAnswer = input()
if userAnswer == "Africa" or userAnswer == "africa":
  print("You aced this quiz!")
else:
  print("that's too bad!")