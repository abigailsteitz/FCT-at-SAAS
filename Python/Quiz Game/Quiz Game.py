#Personality Quiz
print("Hello World!")

print("Welcome to a quiz on Eva. It's time to see how good a friend you really are.")

score = 0

userAnswer = input("How old is Eva?")
print(userAnswer)

if userAnswer == "15" or userAnswer == "fifteen" or userAnswer == "Fifteen":
  print("Correct; the first question is always easy.")
  score += 1
  print("You have " + str(score) + " out of 7 correct.")

else:
  print("You got the first question wrong - not a strong start.")

userAnswer = input("What is Eva's birthday?")
print(userAnswer)

if userAnswer == "May 31" or userAnswer == "May 31st" or userAnswer == "may 31" or userAnswer == "may 31st":
  print("Phew, I was worried you would forget.")
  score += 1
  print("You have " + str(score) + " out of 7 correct.")
  
else:
    print("Oooohh, that's incorrect. Maybe don't tell her though.")
    
userAnswer = input("What is Eva's dream job?")
print(userAnswer)

if userAnswer == "Journalist" or userAnswer == "journalist" or userAnswer == "Editor" or userAnswer == "editor":
    print("Correct, although that was an easy one.")
    score += 1
    print("You have " + str(score) + " out of 7 correct.")
    
else:
  print("How did you get that wrong?")
  
userAnswer = input("What is her favorite thing to draw?")
print(userAnswer)

if userAnswer == "architecture" or userAnswer == "buildings" or userAnswer == "Architecture" or userAnswer == "Buildings":
  print("Good! That was a more difficult question.")
  score += 1
  print("You have " + str(score) + " out of 7 correct.")
  
else:
  print("No, but it's less expected you know that.")
  
userAnswer = input("Does Eva speak French?")
print(userAnswer)

if userAnswer == "yes" or userAnswer == "Yes" or userAnswer == "Oui" or userAnswer == "oui":
  print("C'est exact!")
  score += 1
  print("You have " + str(score) + " out of 7 correct.")

else:
  print("Pas bon!")
  
userAnswer = input("What is Eva's article about in 1 word?")
print(userAnswer)

if userAnswer == "AI" or userAnswer == "Ai" or userAnswer == "ai":
  print("You must be an Eva expect. Good job on reading the article.")
  score += 1
  print("You have " + str(score) + " out of 7 correct.")

else:
  print("Go read her article!")
  
userAnswer = input("Finally, what fictional character does Eva want to embody?")
print(userAnswer)

if userAnswer == "Rory Gilmore" or userAnswer == "rory gilmore":
  print("That's right, it is easy to tell?")
  score += 1
  print("You have " + str(score) + " out of 7 correct.")
  
else:
  print("Incorrect, go watch Gilmore Girls.")
  
print("Thank you for playing!")
print("You ended with " + str(score) + " out of 7 correct.")
if score == 7:
  print("Wow, a perfect score! You must have good memory or you know her really well.")
elif score == 5 or score == 6:
  print("Pretty close, nice job.")
elif score == 4:
  print("You got half! That's... okay I guess.")
elif score == 2 or score == 3:
  print("Wow that's a low score. You should go say hi to her.")
elif score == 1:
  print("You only got 1? Go ask her how her day was or something and come back to get a higher score.")
elif score == 0:
  print("You actually got nothing right. Do you even know her?")