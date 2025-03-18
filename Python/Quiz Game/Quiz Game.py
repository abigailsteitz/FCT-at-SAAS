print("hello world!")

print("Only 1 in 20 people can get 5/5 on this test about Flowers... Are you ready to begin?")
print("  ")
userAnswer = input("  ")
if userAnswer == "No":
  print(" ")
  print(":(")
else:
  print(" ")
  print("Okay lets go!")
  
print("please note that no capital letters will be needed to answer questions correctly")
print("  ")
print("lets get started:")

score = 0

print(" ")
print("What type of flower do people commonly give their Significant Other?")
print(" ")
userAnswer = input("  ")

if userAnswer == "roses":
  print(" ")
  print("✅ Correct! :)")
  score += 1
else:
  print(" ")
  print("❌ incorrect :(")
  print("the correct answer was roses")  
  
print(" ")  
print("What flower do people use to tell if they like butter or not?")
print("  ")
userAnswer = input("  ")

if userAnswer == "buttercups":
  print(" ")
  print("✅ Correct! :)")
  score += 1
else:
  print(" ")
  print("❌incorrect :(")
  print("the correct answer was buttercups") 
  
print(" ")
print("What is the State flower of Washington?")
print("  ")
userAnswer = input("  ")


if userAnswer == "rhododendron":
  print(" ")
  print("✅ Correct! :)")
  score += 1
else:
  print(" ")
  print("❌ incorrect :(")
  ("the correct answer was rhododendron")
  
print("What flower is named for the greek goddess of the rainbow?")
print(" ")
print("A: Poppies")
print("B: Daisies")
print("C: Hydrangeas")
print("D: Irises")
print("  ")
userAnswer = input(" ")


if userAnswer == "irises":
  print(" ")
  print("✅ Correct! :)")
  score += 1
elif userAnswer == "d":
  print(" ")
  print("✅ Correct! :)")
  score += 1
elif userAnswer == "d: irises":
  print(" ")
  print("✅ Correct!")
  score += 1
elif userAnswer == "d, irises":
  print(" ")
  print("✅ Correct!")
else:
  print(" ")
  print("❌ incorrect :(")
  print("the correct answer was d, irises ")

print(" ")
print("What color Rose is often given as a sign of friendship?")
print("  ")
userAnswer = input("  ")


if userAnswer == "yellow":
  print(" ")
  print("✅ Correct! :)")
  score +=1 
else:
  print(" ")
  print("❌ incorrect :(")
  ("the correct answer was yellow")
  

print("  ")
print("Would you like to answer a bonus challenge question?")
print("please answer yes or no")
print("  ")
userAnswer = input("  ")
if userAnswer == "no":
  print(" ")
  print("Ok, thanks for playing!")
  print("you got " + str(score) + "/5 right!")
  print(" ")
  print(" ")
  print("goodbye!")
else:
  print(" ")
  print("ok here it is:")

  print(" ")
  print("In Holland, what flower used to be more valuable than gold?")
  print(" ")
  print("A: Daffodils")
  print("B: Tulips")
  print("C: Gladiolus")
  print("D: Carnations")
  print("  ")
  userAnswer = input(" ")

  if userAnswer == "tulips":
    print(" ")
    print("✅ Correct! :)")
    score += 1
  elif userAnswer == "b":
    print(" ")
    print("✅ Correct! :)")
    score += 1
  elif userAnswer == "b: tulips":
    print(" ")
    print("✅ Correct!")
    score += 1
  elif userAnswer == "b, tulips":
    print(" ")
    print("✅ Correct!")
    score += 1
  else:
    print(" ")
    print("❌ incorrect :(")
    ("the correct answer was tulips")

  print(" ")
  print("Thank you so much for playing")
  print("you got " + str(score) + "/6 right!")
  print("goodbye!")