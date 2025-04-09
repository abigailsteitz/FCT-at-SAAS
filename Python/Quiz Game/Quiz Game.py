print ("Hello world")
print ("welcome to a quiz about my dog" )

score = 0

# this is a variable
userAnswer = input("what type of dog is he?")
print (userAnswer)

# this is conditional
if userAnswer == "Shitzu":
  print("Good job")
  score = score + 10000
else:
  print("WRONG")
  
userAnswer = input("What is his name")

# this is conditional
if userAnswer == ("Myles"):
  print("Yes!")
  score += 10000
else: 
  print("hmmm")
  print("you're wrong")
  
# this is a variable
userAnswer = input("when is his birthday?")
print (userAnswer)

# this is conditional
if userAnswer == "dec 21" or userAnswer == "11/21":
  print("correct!")
  score = score + 10000
else:
  print("wrong!!")
  
# this is a variable
userAnswer = input("how much does he weigh?")
print (userAnswer)

# this is conditional
if userAnswer == "8 lbs" or userAnswer == "8 pounds":
  print("danggg niceee")
  score = score + 10000
  
  # this is a variable
userAnswer = input("whats his favorite activity?")
print (userAnswer)

# this is conditional
if userAnswer == "sleep" or userAnswer == "play":
  print("yesss")
  score = score + 10000

print("score is")
print(score)
