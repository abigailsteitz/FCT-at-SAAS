# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch.

# First day; Ask your user questions, if their answer using the
# input() function, and tell them if they got the answer right or wrong.
print("Hello World!")

print("Welcome to my quiz about soccer")

score = 0

# Ask the user a question
print("Who is the best Soccer player in the world?")

# get their answer
userAnswer = input()
print(userAnswer)

# check if it's correct
# This is called a conditional
if userAnswer == "Ronaldo" or "Messi":
  print("Correct")
  score = score + 1
  print("You got " +str(score) + " out of 5 correct")
else:
  print ("Incorrect")
 
 # Ask the user a question
print("What is the best team?")
# get their answer
userAnswer = input()
  
   # check if it's correct
# This is called a conditional
if userAnswer == "Real Madrid":
  print("Correct")
  score = score + 1
  print("You got " +str(score) + " out of 5 correct")
else:
  print ("Incorrect")
  
  
  # Ask the user a question
print("Who has the most goals in Soccer history?")
# get their answer
userAnswer = input()
  
 # check if it's correct
# This is called a conditional
if userAnswer == "Messi":
  print("Correct")
  score = score + 1
  print("You got " +str(score) + " out of 5 correct")
else:
  print ("Incorrect")
  
  # Ask the user a question
print("What is Ronaldo's first name?")
# get their answer
userAnswer = input()
  
 # check if it's correct
# This is called a conditional
if userAnswer == "Christiano":
  print("Correct")
  score = score + 1
  print("You got " +str(score) + " out of 5 correct")
else:
  print ("Incorrect")
  
  # Ask the user a question
print("Who won the 2022 world cup?")
# get their answer
userAnswer = input()
  
# check if it's correct
# This is called a conditional
if userAnswer == "France":
  print("Correct")
  score = score + 1
  print("You got " +str(score) + " out of 5 correct")
else:
  print ("Incorrect")