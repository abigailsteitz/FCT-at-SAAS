print("Hello World!")

print("Welcome to my quiz about dogs! I hope you enjoy and have fun!!")

print("Q1:What dog breed is the largest?")
score = 0
print("a) Great dane")
print("b) Golden doodle")

useranswer = input()

if useranswer == "a":
  print("Yes,that is correct!")
  score = score + 1
elif useranswer == "b":
  print("Nope, good try")
else:
  print("What did you type???")
  
print("Q2:What dog breed did Cruella De Vil want to make coats out of?") 
print("a) Dalmation")
print("b) Collie")

useranswer = input()

if useranswer == "a":
  print("Slay queen, that is correct!")
  score = score + 1
elif useranswer == "b":
  print("Sorry, that is not correct")
else:
  print("What did you type???")

print("Q3:What is the smallest dog breed?")
print("a) Bernese Mountain Dog")
print("b) Chihuaua")

useranswer = input()

if useranswer == "b":
  print("Yes, that is true!")
  score = score + 1
elif useranswer == "a":
  print("Sorry that is incorrect")
else:
  print("What did you type??")
  
print("Q4:Are puppies born deaf?")
print("a) Yes")
print("b) No")

useranswer = input()

if useranswer == "a":
  print("Yep!")
  score = score + 1
elif useranswer == "b":
  print("No!")
else:
  print("What did you type??")
  
print("Q5:What is the most popular dog breed in the world?")
print("a) French bulldog")
print("b) Golden retriever")

useranswer = input()

if useranswer == "a":
  print("You're right!")
  score = score + 1
elif useranswer == "b":
  print("Sorry, that is incorrect")
else:
  print("What did you type?")
  
print("Great job! You got " + str(score) + " out of 5 correct! Thank you for playing!")# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch.