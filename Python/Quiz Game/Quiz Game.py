# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch.
print("Welcome to my quiz")
score = 0
print ("First question is...")

print("what is 5 times 5?")
print ("a) 25")
print ("b) 10")
userAnswer = input ()
print(userAnswer)

if userAnswer == "a":
  print("Correct")
  score = score + 1
elif userAnswer == "b":
  print("Incorrect")
print("what is 10 plus 10?")
print ("a) 100")
print ("b) 20")
userAnswer = input ()
print(userAnswer)

if userAnswer == "b":
  print("Correct")
  score = score + 1
elif userAnswer == "a":
  print("Incorrect")
print("what is 42 divided by 6?")
print ("a) 8")
print ("b) 7")
userAnswer = input ()
print(userAnswer)

if userAnswer == "b":
  print("Correct")
  score = score + 1
elif userAnswer == "a":
  print("Incorrect")
  
print("what is the square root of 48x ?")
print ("a) 4x")
print ("b) 4 square root 3x")
userAnswer = input ()
print(userAnswer)

if userAnswer == "b":
  print("Correct")
  score = score + 1
elif userAnswer == "a":
  print("Incorrect")
  
print("what is the ph of bleach ?")
print ("a) 11-13")
print ("b) 9-10")
userAnswer = input ()
print(userAnswer)

if userAnswer == "a":
  print("Correct")
  score = score + 1
elif userAnswer == "b":
  print("Incorrect")
  
print("largest island in caribbean?")
print ("a) cuba")
print ("b) jamaica")
userAnswer = input ()
print(userAnswer)

if userAnswer == "a":
  print("Correct")
  score = score + 1
elif userAnswer == "b":
  print("Incorrect")

  
print("What is the official language of Egypt??")
print ("a) arabic")
print ("b) eygyptian")
print ("c) english")
userAnswer = input ()
print(userAnswer)

if userAnswer == "a":
  print("Correct")
  score = score + 1
elif userAnswer == "b":
  print("Incorrect")


print("What is the official language of india??")
print ("a) hindi")
print ("b) english")
print ("c) hindi and english")
userAnswer = input ()
print(userAnswer)

if userAnswer == "c":
  print("Correct")
  score = score + 1
elif userAnswer == "b":
  print("Incorrect")
elif userAnswer == "c":
  print("Incorrect")
print ("You got aa" + str(score) + " correct out of 8!")