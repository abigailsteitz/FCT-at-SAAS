score = 0

print("Hello World!")

print("Welcome to my quiz about Henry's at SAAS!")

# Ask the user a question
print("Whos the tallest Henry?")
print("- Henry Finkelman")
print("- Henry Kaplan")
print("- Henry Moore")
print("- Henry Predmore")
# get their answer

userAnswer = input()
if userAnswer == "Henry Kaplan":
  print("NICE JOB BUCKO!")
  score += 1
else:
  print("WRONG, The right answer was Kaplan")
  
# Ask the user a question
print("Whos the shortest Henry?")
print("- Henry Finkelman")
print("- Henry Kaplan")
print("- Henry Moore")
print("- Henry Predmore")
# get their answer
userAnswer = input()
print(userAnswer)

# check if it's correct
# This is called a conditional
if userAnswer == "Henry Finkelman":
  print("WOWZERS!")
  score += 1
else:
  print("WRONG, The right answer was Finkelman")
  
  # Ask the user a question
print("Whos the strongest Henry?")
print("- Henry Finkelman")
print("- Henry Kaplan")
print("- Henry Moore")
print("- Henry Predmore")
# get their answer
userAnswer = input()
print(userAnswer)

# check if it's correct
# This is called a conditional
if userAnswer == "Henry Moore":
  print("Splendid Job Son!")
  score += 1
else:
  print("WRONG, The right answer was Moore")
  
  # Ask the user a question
print("Whos the Henry in 6th grade?")
print("- Henry Finkelman")
print("- Henry Kaplan")
print("- Henry Moore")
print("- Henry Predmore")
# get their answer
userAnswer = input()
print(userAnswer)

# check if it's correct
# This is called a conditional
if userAnswer == "Henry Finkelman":
  print("WOO HOO!")
  score +=1
else:
  print("WRONG, The right asnwer was Finkelman")
  
  # Ask the user a question
print("Whos the craziest Henry?")
print("- Henry Finkelman")
print("- Henry Kaplan")
print("- Henry Moore")
print("- Henry Predmore")
# get their answer
userAnswer = input()
print(userAnswer)

# check if it's correct
# This is called a conditional
if userAnswer == "Henry Predmore":
  print("BAZANGA!")
  score += 1
else:
  print("WRONG, The right answer was Predmore")
  
print("Thank you for completing this quiz!")
print("Your score was " + str(score) + " out of 5 questions correct")
if score < 3:
  print("You did not do very well.")
else:
  print("You did pretty well! Good job!")