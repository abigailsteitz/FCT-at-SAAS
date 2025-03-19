# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch.
print("Hello World!")
print("Welcome to my quiz about me, Rahul.")
print("Answer with either 'a' or 'b' (lowercase letter) or with the same text as written.")
score = 0
#set score to 0
print("Q1: What is my birthday?")
print("a) February 13")
print("b) June 29")
print("c) October 6")
print("d) November 14")
userAnswer = input()
if userAnswer =="b" or userAnswer =="June 29":
  print("You got it correct!")
  score = score + 1
#add points if they get it correct
else:
    print("wrong")

print("Q2: What is my favorite color?")
print("a) red")
print("b) blue")
print("c) green")
print("d) white")
userAnswer = input()
if userAnswer =="b" or userAnswer =="blue":
  print("correct")
  score = score + 1
else:
  print("sorry thats wrong")
  
print("Q3: Do I have siblings?")
print("a) yes")
print("b) no")
userAnswer = input()
if userAnswer =="a" or userAnswer =="yes":
  print("nice job")
  score = score + 1
else:
  print("sorry, thats wrong")
  
print("Q4: Do I have a pet?")
print("a) yes")
print("b) no")
print("c) yes, 1 pet")
print("d) yes, 2 pets")
userAnswer = input()
if userAnswer =="b" or userAnswer =="no":
  print("correct")
  score = score + 1
else:
  print("wrong")

print("Q5:How old am I?")
print("a) 13")
print("b) 14")
print("c) 15")

print("d) 16")
userAnswer = input()
if userAnswer =="b" or userAnswer =="14":
  print("nice, thats correct")
  score = score + 1
else:
  print("sorry thats wrong")
#bonus if they got all 5
if score == 5:
  print("Since you got all 5 questions right, here's a bonus question!")
  print("What's my favorite fruit?")
  print("a) strawberries")
  print("b) apples")
  print("c) mangoes")
  print("d) watermelon")
  userAnswer = input()
  if userAnswer =="c" or userAnswer =="mangoes":
    print("Wow, thats correct!")
    score = score + 1
  else:
    print("nice try, but that's incorrect!")

print("You got " + str(score) + " questions correct!")
print("Thank's for playing!")