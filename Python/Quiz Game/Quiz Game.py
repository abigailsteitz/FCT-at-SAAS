

print ("Welcome to My Quiz About Ian")
userAnswer = input("What is Ian's Birthday")
print(userAnswer) 

score = 0 
# this is a conditional
if userAnswer == "Aug 9" or userAnswer == "8/9" or userAnswer == "August 9th" or userAnswer == "aug 9" or userAnswer == "august 9" or userAnswer == "august 9th":
  print("GOOD")
  score = score + 1
  print("You got " + str(score) + " out of five correct")
else:
    print("BAD")
    
userAnswer = input("How Tall is Ian?")
print(userAnswer) 

if userAnswer == "5'8" or userAnswer == "five eight" or userAnswer == "short":
  print("GOOD")
  score += 1
  
else:
    print("BAD")
    
userAnswer = input("What Instrument Does Ian Play?")
print(userAnswer) 

if userAnswer == "Saxaphone" or userAnswer == "Tenor Saxophone" or userAnswer == "sax" or userAnswer == "Tenor Sax":
  print("GOOD")
  score += 1
else:
    print("BAD")
    
userAnswer = input("What NESE is he?")
print(userAnswer) 

if userAnswer == "Chinese":
  print("GOOD")
  score += 1
else:
    print("BAD")
    
userAnswer = input("What is his Block 4?")
print(userAnswer) 

if userAnswer == "Math" or userAnswer == "Precalculus":
  print("GOOD")
  score += 1
else:
    print("BAD")
    

print("You got " + str(score) + " out of fiveaug 9")