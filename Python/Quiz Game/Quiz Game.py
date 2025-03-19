# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch
print("Hello World")

print("Welcome to my quiz about me")

# Ask the user a question
print("What is my birthday")

# get answer
userAnswer = input()
print(userAnswer)

if userAnswer == "June 10" or userAnswer == "6/10" or userAnswer == "june 10":
  print("Bingo")
else:
  print("NO!!!!")
  
# Question 2

print("What my favorite food, is it")
print("A: Steak")
print("B: Sushi")
print("C: Pasta")
# get answer
userAnswer = input()
if userAnswer == "A" or userAnswer == "a" or userAnswer == "Steak":
  print("Correct!")
else:
  print("Way off buddy, better luck next time")




# Question 3
print("Can you guess my favorite color?")
print("A: Red")
print("B: Blue")
print("C: Purple")
# get answer
userAnswer = input()
if userAnswer == "C" or userAnswer == "c" or userAnswer == "Purple":
  print("Nice Job!")
else:
  print("Not even close")



# Question 4
print("Gambling moment, Heads or Tails")
print("Heads")
print("Tails")
# get answer
userAnswer = input()
if userAnswer == "Heads" or userAnswer == "heads" or userAnswer == "head":
  print("Casino Time!")
else:
  print("Stay away from the slot machines")



# Question 5

print("Theres only 1 right answer, A, B, Or C. 1 in 3 odds, except its not B ;)")
# get answer
userAnswer = input()
if userAnswer == "A" or userAnswer == "a":
  print("You beat the odds")
elif userAnswer == "B" or userAnswer == "b":
  print("I told you its not this, you got trust issues or something?")
else:
  print("Way off buddy, better luck next time")