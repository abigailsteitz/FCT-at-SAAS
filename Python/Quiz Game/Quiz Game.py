print("welcome to the quiz about dogs!")
score = 0

print("Q1: What is the name of the biggest dog in the world?")
print("a) Zeus")
print("b) Jonathon")
print("c) Hercules")

userAnswer = input()
print(userAnswer)

if userAnswer == "a":
  print("That is fantastic!")
  score = score + 1
elif userAnswer == "b":
  print ("Nope")
elif userAnswer== "c":
  print("Nope")
else:
  print("Huh?")
  
print("Q2: What dog breed did Cruella De Vil want to make coast out of")
print("a) Golden Retrever")
print("b) Dalmation")
print("c) Chiwawa")

userAnswer = input()

if userAnswer == "b":
  print("That is FANTASTIC!")
  score = score + 1
elif userAnswer == "b":
  print ("Nope")
elif userAnswer== "c":
  print("Nope")
else:
  print("Huh?")

print("Q3: What is the name of the smallest dog in the world?")
print("a) Tinky Winky")
print("b) Tinny Tim")
print("c) Miracle Milly")

userAnswer = input()

if userAnswer == "c":
  print("That is fantastic!")
  score = score + 1
elif userAnswer == "b":
  print ("Nope")
elif userAnswer== "a":
  print("Nope")
else:
  print("Huh?")
  
print("Q4: Are puppies born deaf?")
print("a)Yes")
print("b)No")

userAnswer = input()

if userAnswer == "a":
  print("That is fantastic!")
  score = score + 1
elif userAnswer == "b":
  print ("Nope")
  
print("Q5: What is the most popular dog breed?")
print("a) Golden Retriever")
print("b) French Bulldog")
print("c) Poodle")

userAnswer = input()

if userAnswer == "b":
  print("That is fantastic!")
  score = score + 1
elif userAnswer == "c":
  print ("Nope")
elif userAnswer== "a":
  print("Nope")
else:
  print("Huh?")
  
print("Great Job! You got " + str(score) + " correct!")
