# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch.
print("Hello")
print("Welcome to my SAAS quiz. To answer you must put in the words after a) or b). This quiz is case sensitive so be extra careful that things are the way you want them to be. There is a bonus question if you get all the questions correct.")
print("Q1: When was the first graduating class?")
score = 0
#multipule choice/1987 is correct
print("a) 1979")
print("b) 1984")
print("c) 1987")
print("d) 1992")
userAnswer=input()
#tell user if they got it correct
#this is called a conditional
if userAnswer == "1984":
  print("Good Job!")
  score = score + 1
elif userAnswer == "1979":
  print("Better luck next time")
elif userAnswer == "1987":
  print("Better luck next time")
elif userAnswer == "1992":
  print("Better luck next time")
else:
  print("Ummm, what?")

print("Q2: When was SAAS founded?")
print("a) 1988")
print("b) 1979")
print("c) 1975")
print("d) 1983")
userAnswer=input()
if userAnswer == "1983":
  print("Good Job!")
  score = score + 1
elif userAnswer == "1979":
  print("Better luck next time")
elif userAnswer == "1988":
  print("Better luck next time")
elif userAnswer == "1975":
  print("Better luck next time")
else:
  print("Ummm, what?")
  
print("Q3: How many kids were in the first graduating class?")
print("a) 72")
print("b) 15")
print("c) 49")
print("d) 5")
userAnswer=input()
if userAnswer == "15":
  print("Good Job!")
  score = score + 1
elif userAnswer == "72":
  print("Better luck next time")
elif userAnswer == "49":
  print("Better luck next time")
elif userAnswer == "5":
  print("Better luck next time")
else:
  print("Ummm, what?")
  
print("Q4: What/where was the first building?")
print("a) Vanderbilt")
print("b) Madision")
print("c) Temple")
print("d) None of these")
userAnswer=input()
if userAnswer == "Temple":
  print("Good Job!")
  score = score + 1
elif userAnswer == "Vanderbilt":
  print("Better luck next time")
elif userAnswer == "Madision":
  print("Better luck next time")
elif userAnswer == "None of these":
  print("Better luck next time")
else:
  print("Ummm, what?")
  
print("Q5: How many different heads of school have there been?")
print("a) 2")
print("b) 3")
print("c) 4")
print("d) 5")
userAnswer=input()
if userAnswer == "3":
  print("Good Job!")
  score = score + 1
elif userAnswer == "2":
  print("Better luck next time")
elif userAnswer == "4":
  print("Better luck next time")
elif userAnswer == "5":
  print("Better luck next time")
else:
  print("Ummm, what?")
#if score =5 then print question 6  
if score == 5:
  print("You got them all correct. Here is a hard question.")
  print("Q6: SAAS is ranked ______ best private high school in Washington State.")
  print("a) 1st")
  print("b) 15th")
  print("c) 7th")
  print("d) 13th")
  userAnswer=input()
  if userAnswer == "7th":
   print("Good Job!")
   score = score + 1
  elif userAnswer == "15th":
   print("Better luck next time")
  elif userAnswer == "1st":
    print("Better luck next time")
  elif userAnswer == "13th":
    print("Better luck next time")
  else:
    print("Ummm, what?")
print ("You got " + str(score) + " correct!")
print ("Press enter to close out of this quiz.")
userAnswer=input()