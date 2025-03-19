# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch.

print("Hello World!")
print("Welcome to my basketball quiz")
print("Q1:Who is the goat of basketball? ")
print("a) Micheal Jordan")
print("b)Lebron James")
print("When you answer, please type the variable.")
# this is a variable which hold's the user's input (box in memory) 
userAnswer = input().lower()
print (userAnswer)

# Telling the user they got it correct. This is called a conditional 
if userAnswer == "b":
  print("Yes!Lebron IS the GOAT")
elif userAnswer == "a":
  print("No.")
else:
  print("Please type again")
  
  
print("Q2:Who won the championship last year? ")
print("a) Celtics")
print("b)Lakers")
print("When you answer, please type the variable.")
# this is a variable which hold's the user's input (box in memory) 
userAnswer = input().lower()
print (userAnswer)

# Telling the user they got it correct. This is called a conditional 
if userAnswer == "b":
  print("Nope!")
elif userAnswer == "a":
  print("Yes!!!!")
else:
  print("Please type again")
  
print("Q3:Who won MVP last year? ")
print("a) Nikola Jokic")
print("b) Paulo Banchero")
# this is a variable which hold's the user's input (box in memory) 
userAnswer = input().lower()
print (userAnswer)

if userAnswer == "b":
  print("Nope!")
elif userAnswer == "a":
  print("Yes!!!!")
else:
  print("Please type again")
  
print("Q4:Who is the All-time scoring leader in the NBA? ")
print("a) Kareem Abdul-Jabar")
print("b) Lebron James ")
# this is a variable which hold's the user's input (box in memory) 
userAnswer = input().lower()
print (userAnswer)

if userAnswer == "b":
  print("Yes! GOAT")
elif userAnswer == "a":
  print("No.")
else:
  print("Please type again")
  
print("Q5:Who leads the NBA in triple-doubles? ")
print("a) Russel Westbrook")
print("b) Oscar Robertson")
# this is a variable which hold's the user's input (box in memory) 
userAnswer = input().lower()
print (userAnswer)

if userAnswer == "b":
  print("Nope, but he was for a long time")
elif userAnswer == "a":
  print("Yes! He leads with 202 career tripple doubles.")
else:
  print("Please type again")
  
  
print("thank you very much for playing and I hope you did well or learned something new. Have a good day!")
