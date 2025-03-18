#GOAL: First day: ask your user questions
print("Hello world")

print("Welcome to my quiz about Lacrosse")

score = 0

userAnswer= input("How many people are on the feild at once for each team")
print(userAnswer)
if userAnswer== "10" or userAnswer=="ten":
  print("Nice")
  score= score + 1

else:
  print("WRONG")
userAnswer= input("How many main positions are there")
print(userAnswer)
if userAnswer== "4" or userAnswer=="four":
  print("Nice")
  score+= 1
  
else:
  print("WRONG")
userAnswer= input("True or false: lacrosse was orininally a native american sport")
print(userAnswer)
if userAnswer== "true" or userAnswer=="yes":
  print("Nice")
  score+= 1
else:
  print("WRONG")
userAnswer= input("True or false: girls and boys lacrosse are the same sport")
print(userAnswer)
if userAnswer== "false" or userAnswer=="no":
  print("Nice")
  score+= 1
else:
  print("WRONG")
userAnswer= input("True or false:Lacrosse is more popular on the East Coast")
print(userAnswer)
if userAnswer== "true" or userAnswer=="yes":
  print("Nice")
  score+= 1
else:
  print("WRONG")
  
print("Quiz complete! Your final score is " +str(score)+ " Out of 5. Thanks for playing!")