#1 Goal: if they got the answer right or wrong.
print("hello world")
print("welcome to my quiz about pigs")

score =0

userAnswer = input("what color are pigs")
print(userAnswer)

# this is a conditional
if userAnswer == "pink":
  print ("nice job")
  score = score + 5
else: 
  print("wrong")
    
    
userAnswer = input("what is the best animal")
print(userAnswer)

# this is a conditional
if userAnswer == "pigs":
  print ("nice job")
else:
    print("wrong")
    
    
userAnswer = input("are pigs smart")
print(userAnswer)

# this is a conditional
if userAnswer == "yes":
  print ("nice job")
else:
    print("wrong")
    
userAnswer = input("can pigs get sunburnt")
print(userAnswer)

# this is a conditional
if userAnswer == "yes":
  print ("nice job")
else:
    print("wrong")
    
userAnswer = input("are pigs animals")
print(userAnswer)

# this is a conditional
if userAnswer == "yes":
  print ("nice job")
else:
    print("wrong")
    
print ("the end")
print ("you got " + str(score) + " out of 5")