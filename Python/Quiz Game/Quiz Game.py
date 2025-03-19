print("welcome to my quiz")

score = 0

#question 1
print("what's my name?")

userAnswer = input()

if userAnswer == "Lily" or userAnswer == "lily":
  print("yes! :)")
  score = score + 1
 
else:
  print("no >:(")

#question 2
print("what's my favorite color?")

userAnswer = input()

if userAnswer == "Red" or userAnswer == "red":
  print("yes! :)")
  score = score + 1
else:
  print("no >:(")
  
#question 3
print("what's my favorite animal?")

userAnswer = input()

if userAnswer == "Cat" or userAnswer == "cat" or userAnswer == "Kitty" or userAnswer == "kitty":
  print("yes! :)")
  score = score + 1
else:
  print("no >:(")
  
#question 4
print("what sport do i play?")

userAnswer = input()

if userAnswer == "Soccer" or userAnswer == "soccer":
  print("yes! :)")
  score = score + 1
else:
  print("no >:(")
  
#question 5
print("who's my best friend?")

userAnswer = input()

if userAnswer == "Julia" or userAnswer == "julia":
  print("yes! :)")
  score = score + 1
else:
  print("no >:(")
  
print("You got " + str(score) + " out of 5 correct")
  
print("the end! thanks for taking this!")