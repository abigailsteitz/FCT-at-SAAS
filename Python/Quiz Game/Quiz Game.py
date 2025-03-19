# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch.
print ("Hello")
print ("Welcome to my geography quiz")
print ("The first question is")
score = 0
print ("Q1: What is the capital of france")
print ("a. Yoshi Gopal")
print ("b. Paris")
print ("c. Rome")
print ("d. Vienna")
userAnswer = input()
print (userAnswer)
if userAnswer == "b" or userAnswer == "B":
  print ("Very good")
  score = score + 1
elif userAnswer == "d" or userAnswer == "D" or userAnswer == "c" or userAnswer == "C" or userAnswer == "a" or userAnswer == "A":
  print ("Damn you suck give up now")
else:
  print("Incorrect buddy")
print ("Q2: What is the capital of Vanuatu")
print ("a. Port Vila")
print ("b. Funafuti")
print ("c. Windhoek")
print ("d. 3rd and Pike")
userAnswer = input()
print (userAnswer)
if userAnswer == "a" or userAnswer == "A":
  print ("Nice Job!")
  score = score + 1
elif userAnswer == "d" or userAnswer == "D" or userAnswer == "c" or userAnswer == "C" or userAnswer == "b" or userAnswer == "B":
  print ("Dumbass")
else:
  print("Incorrect buddy")
print ("Q3:What country borders the United Arab Emirates")
print ("a. Montana")
print ("b. Saudi Arabia")
print ("c. Israel")
print ("d. North Korea")
userAnswer = input()
print (userAnswer)
if userAnswer == "b" or userAnswer == "B":
  print ("Hey good job")
  score = score + 1
elif userAnswer == "d" or userAnswer == "D" or userAnswer == "c" or userAnswer == "C" or userAnswer == "a" or userAnswer == "A":
  print ("No")
else:
  print("Incorrect buddy")
print ("Q4: What Team did Khvicha Kvaratskhelia play for in the 2022-2023 season")
print ("a. Djibouti National Team")
print ("b. SAAS JVC Boys Soccer")
print ("c. PSG")
print ("d. Napoli")
userAnswer = input()
print (userAnswer)
if userAnswer == "d" or userAnswer == "D":
  print ("Great Job!")
  score = score + 1
elif userAnswer == "b" or userAnswer == "B" or userAnswer == "c" or userAnswer == "C" or userAnswer == "a" or userAnswer == "A":
  print ("Disapointing")
else:
  print("Incorrect buddy")
print ("Q5: What Country has the most islands in the world")
print ("a. Sweden")
print ("b. Bahamas")
print ("c. Indonesia")
print ("d. China")
userAnswer = input()
print (userAnswer)
if userAnswer == "a" or userAnswer == "A":
  print ("Very Impressive!")
  score = score + 1
elif userAnswer == "b" or userAnswer == "B" or userAnswer == "c" or userAnswer == "C" or userAnswer == "d" or userAnswer == "D":
  print ("Bruh")
else:
  print("Incorrect buddy")
print ("Q6: Where is the space needle")
print ("a. Korea")
print ("b. Paradise Palms")
print ("c. 47.6205° N, 122.3493° W")
print ("d. Western Siberia")
userAnswer = input()
print (userAnswer)
if userAnswer == "c" or userAnswer == "C":
  print ("Nice Job")
  score = score + 1
elif userAnswer == "b" or userAnswer == "B" or userAnswer == "a" or userAnswer == "A" or userAnswer == "d" or userAnswer == "D":
  print ("Bruh")
else:
  print("Incorrect buddy")
print ("you scored " + str(score) + " points out of 6")
if score == 6 or score == 5:
  print ("BONUS QUESTION")
  print ("Where is the amazon rainforest")
  print ("a. Brazil")
  print ("b. North Africa")
  print ("c. Moisty Mire")
  print ("d. China")
  userAnswer = input()
  print (userAnswer)
  if userAnswer == "a" or userAnswer == "A":
    print ("Phenomenal!")
  elif userAnswer == "b" or userAnswer == "B" or userAnswer == "c" or userAnswer == "C" or userAnswer == "d" or userAnswer == "D":
   print ("Bruh")
  else:
    print("Incorrect buddy")