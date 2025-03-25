# First code in Python
# Explanation
print("")
print("Welcome to The Trivia Game!!");

# Score set up
score = 0

# Start
print("");
print("The goal is to answer questions correctly. Some questions are fill in the blanks and others are just trivia. If you get everything right you get a bonus question!")
print("Please capitalize any answers that are names.")
print("")
print("Type OK, to Start!")
print("")

# use conditional
while True:
  userAnswer = input();
  if userAnswer.lower() == "ok":
# can have multiple right answers if you write "or" then the function again
   print("")
   print("Lets begin.");
   break
  else:
   print("")
   print("Type OK, to Start!")
   print("")

  
# Question 1
print("")
print("Question 1.")
print("That which does not kill us makes us ______")
print("")
# Answer 1
userAnswer = input()
#  Correct? 1
if userAnswer.lower() == "stronger" :
  print("")
  print("Great, you got it!")
  print("")
  # Score increse
  score += 1
else:
  print("")
  print("Nope! The answer was 'stronger'")
  print("")
  
# Question 2
print("Question 2.")
print("Alright, what are the spikes on a fork called?")
print("")

# Answer 2
userAnswer = input()

# Correct? 2
if userAnswer.lower() == "tine" or userAnswer.lower() == "a tine" or userAnswer.lower() == "tines":
  print("")
  print("Yes!")
  print("")
  # Score increse
  score += 1
else:
    print("")
    print("No, sorry. They are Tines.")
    print("")

# Question 3
print("Question 3.")
print("What does the 'Ides of March' simbolize in history?")
print("")

# Answer 3
userAnswer = input()

# Correct? 3
answer = userAnswer

word_to_check = "aesar"
if word_to_check in userAnswer:
  print("")
  print("You got it!")
  print("")
  # Score increase
  score += 1
else:
  print("")
  print ("Almost... Next time!! It simbolizes the death of Caesar!")
  print("")

# Question 4 
print("Question 4.")
print ("What is the more scientific name for the knee cap?")
print("")

# Answer 4
userAnswer = input()

# Correct? 4
if userAnswer.lower() == "patella" or userAnswer.lower() == "patela":
  print("")
  print("Yes! I'm suprised you knew that!")
  print("")
  # Score increase
  score += 1
else:
  print("")
  print("Good guess, so close! A knee cap is a patella. Keep going!")
  print("")
  
# Question 5 
print("Question 5.")
print("Whitch god created horses in Greek mythology?")
print("")

# Answer
userAnswer = input()

# Correct? 5
if userAnswer.lower() == "poseidon" or userAnswer.lower() == "sea god" or userAnswer.lower() == "the god of the sea" or userAnswer.lower() == "posiden" or userAnswer.lower() == "posidan":
  print("")
  print("Yeah! Weird right?")
  print("")
  # Score increase
  score += 1 
elif userAnswer.lower() == "neptune":
  print("")
  print("Actually that is the Roman version. The GREEK god who created horses was Poseidon, the god of the sea! this is only half a point. Really close!")
  print("")
  score += .5
else:
  print("")
  print("The answer was Poseidon! Great job trying!")
  print("")
  
# Bonus question
if score == 5:
  print("You made it to the bonus question! Great job.")
  print("")
  print("Bonus Question.")
  print("What is the most agressive species of jellyfish?")
  print("")
  userAnswer = input()
  if userAnswer.lower() == "box jellyfish" or userAnswer.lower() == "box" or userAnswer.lower() == "box jelly fish" or userAnswer.lower() == "box jelyfish":
    # Score up
    score += 1
    print("")
    print("Great job on the last question!")
    print("")
    print("Your overall score is {} out of 6!".format(score))
    print("")
  else:
    print("")
    print("Great effort on the super tricky bonus question! Next time you'll get it!")
    print("")
    print("Your super awesome score is {}!".format(score))
    print("")
    print("If you want to try again feel free. Just tap on run!")
else:
  print("")
  print("")
  print("You did amazing! You scored {} points in all!".format(score))
  print("")
  print("If you want to try again just click on run!!")
  print("")
  
# You can also give multiple choice questions by printing something like a) and b) then writing "if userAnswer == "a":  else: