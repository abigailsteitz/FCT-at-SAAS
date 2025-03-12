print("Star Wars Quiz")

score = 0 
print("What is your name?")
input()

print("What color is Yoda's lightsaber?")
userAnswer = input()
if userAnswer.lower() == "green":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The answer was green.")

print("What is the name of Han Solo's co-pilot?")
userAnswer = input()
if userAnswer.lower() == "chewbacca" or userAnswer.lower() == "chewie":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The answer was Chewbacca.")

print("What is the name of the small, green Jedi Master?")
userAnswer = input()
if userAnswer.lower() == "yoda":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The answer was Yoda.")

print("What is the name Darth Vaders Child?")
userAnswer = input()
if userAnswer.lower() == "Luke Skywalker" or userAnswer.lower() == "Luke":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The answer was Luke Skywalker.")

print("What species is Jabba the Hutt?")
userAnswer = input()
if userAnswer.lower() == "hutt":
  print("Correct!")
  score += 1
else:
  print("Incorrect! The answer was Hutt.")

print(f"Your final score is {score} out of 5.")



