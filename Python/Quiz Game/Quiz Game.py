print("hello")
print("welcome to my quiz about pigs")

score = 0

userAnswer = input ("what color are pigs?")
print(userAnswer)
if userAnswer == "pink":
  print("nice job")
  score = score + 1
  print("you got " + str(score) + " out of 5 correct")
else:
  print("ur dumb")
  
userAnswer = input ("what is the best animal?")
print(userAnswer)
if userAnswer == "pigs" or userAnswer == "pig" :
  print("nice job")
  score = score + 1
  print("you got " + str(score) + " out of 5 correct")
else:
  print("ur dumb")
  
userAnswer = input ("are pigs smart?")
print(userAnswer)
if userAnswer == "yes":
  print("nice job")
  score = score + 1
  print("you got " + str(score) + " out of 5 correct")
else:
  print("ur dumb")
  
userAnswer = input ("can pigs get sunburnt?")
print(userAnswer)
if userAnswer == "yes":
  print("nice job")
  score = score + 1
  print("you got " + str(score) + " out of 5 correct")
else:
  print("ur dumb")
  
userAnswer = input ("are pigs dirty")
print(userAnswer)
if userAnswer == "no":
  print("nice job")
  score = score + 1
  print("you got " + str(score) + " out of 5 correct")
else:
  print("ur dumb")