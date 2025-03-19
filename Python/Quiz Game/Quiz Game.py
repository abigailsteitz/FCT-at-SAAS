# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch.
# take their answer using the input() function,
# and tell them if they got the answer right or wrong.
score = 0

print("")
print("this is a quiz on saas")

print("Q1: what is the name of our legendary, bald soccer coach?                                               Make sure to answer as *a*, *b*,*c*, or *d*")
print("a) Craig")
print("b) Rob")
print("c) Tom ")
print("d) Thomas")

# this is a variable that holds the user's input
userAnswer = input()
print(userAnswer)

# Tell the user if they got it correct
# This is called a conditional
if userAnswer == "a" or userAnswer == "A":
  print("yup")
  score = score + 1
  
elif userAnswer == "b":
  print("close")
else:
  print("oh nah")


print("Q2: When was basball introduced to Saas sports?")

print("a)1999")
print("b)2029")
print("c)2025")
print("d)1302")


# this is a variable that holds the user's input
userAnswer = input()
print(userAnswer)

# Tell the user if they got it correct
# This is called a conditional
if userAnswer == "c" or userAnswer == "C":
  print("your hella smart")
  score = score + 1
elif userAnswer == "a":
  print("close")
else:
  print("oh nah")


print("Q3: What singing group sings at fallapalooza (fallmania)?")

print("a)the car keys")
print("b)the peaches")
print("c)the smartboards")
print("d)the onions")


# this is a variable that holds the user's input
userAnswer = input()
print(userAnswer)

# Tell the user if they got it correct
# This is called a conditional
if userAnswer == "d" or userAnswer == "D":
  print("your hella smart")
  score = score + 1
elif userAnswer == "a":
  print("close")
else:
  print("oh nah")
  
print("Q4: what two places hold both winter hoopla, and fallpalooza?")

print("a)Temple & Starfire")
print("b)Starfire & highschool gym")
print("c)Tacoma dome & Seattle U")
print("d)Mighty O and Starbucks")


# this is a variable that holds the user's input
userAnswer = input()
print(userAnswer)

# Tell the user if they got it correct
# This is called a conditional
if userAnswer == "b" or userAnswer == "B":
  print("your hella smart")
  score = score + 1
elif userAnswer == "d":
  print("close")
else:
  print("oh nah")

print("Q5: Finally, who is our athletics director?")

print("a)Gudeta")
print("b)The cardinal mascot")
print("c)Shan Peterson")
print("d)Cathy Schick")


# this is a variable that holds the user's input
userAnswer = input()
print(userAnswer)

# Tell the user if they got it correct
# This is called a conditional
if userAnswer == "d" or userAnswer == "D":
  print("your hella smart")
  score = score + 1
elif userAnswer == "a":
  print("ahhhh no.")
else:
  print("oh nah")
print ("You got" + str(score) + "correct!")