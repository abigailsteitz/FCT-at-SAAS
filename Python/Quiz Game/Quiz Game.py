print("Hello World?")

print("This is a quiz about Will Cundiff.")

score=0

# Ask the user a question
print("What's Will's Dad's name?")
print("Tim")
print("Bob")
print("Elliot")
print("Donald")
# get their answer
userAnswer = input()
print(userAnswer)

# check if its correct
# This is called a conditional
if userAnswer == "Elliot" :
  print("Good job")
  score+= 1
else:
  print("Incorrect, the right answer is Elliot")
 
  # Ask the user a question
print("What's Will's main sport?")
print("Lax")
print("Baseball")
print("T-Ball")
print("Pickleball")
# get their answer
userAnswer = input()
print(userAnswer)

# check if its correct
# This is called a conditional
if userAnswer == "Lax" :
  print("Good job")
  score+= 1
else:
  print("Incorrect, the right answer is Lax")
 
  # Ask the user a question
print("What is NOT an ingredient of Lock in juice?")
print("Sugar")
print("Fruit Juice")
print("Caffine")
print("Child Tears")
# get their answer
userAnswer = input()
print(userAnswer)

# check if its correct
# This is called a conditional
if userAnswer == "Child Tears" :
  print("Good job")
  score+= 1
else:
  print("Incorrect, the right answer is Child Tears")
 
  # Ask the user a question
print("What App is he most proficient with")
print("Snapchat")
print("Teamsnap")
print("Flappy Bird")
print("Brawl Stars")
# get their answer
userAnswer = input()
print(userAnswer)

# check if its correct
# This is called a conditional
if userAnswer == "Snapchat" :
  print("Good job")
  score+= 1
else:
  print("Incorrect, the right answer is Snapchat")
 
  # Ask the user a question
print("Where is Cundiff right now?")
print("School")
print("Wisconsin")
print("Emergency Room")
print("White house")
# get their answer
userAnswer = input()
print(userAnswer)

# check if its correct
# This is called a conditional
if userAnswer == "Emergency Room" :
  print("Yes, our best wishes are with him.")
else:
  print("Incorrect, the right answer is the Emergency Room")
print("you got " + str(score) + " Correct")