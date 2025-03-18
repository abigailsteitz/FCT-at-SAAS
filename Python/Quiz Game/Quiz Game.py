score = 0

print("Welcome to the Puget Sound Orcas trivia game!")
print("How many Killer Whales are in J-Pod in the Puget Sound?")
guess = input()
# Turn the string "72" the user typed into the int 72
guessInt = int(guess)

if guessInt == 25:
  print("Yep!")
  score = 1
else:
  print("Nope, sorry")
  
print("Who was the oldest member until 2016? a) Granny b) Matilda c) Gandalf")
oldest = input()

if oldest == "a":
  print("Correct!")
  score = 1
else:
  print("Nope, taking 1,000,000 points off 😲")
  score -=1000000
  
print("Score:")
print(score)