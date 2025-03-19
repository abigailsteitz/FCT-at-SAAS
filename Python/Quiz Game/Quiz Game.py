# This file intentionally empty.
# You should copy-paste your quiz game here!
# Over-write this file in your own branch.
print("🐶 Welcome to the Dog Quiz Game! 🐶")

score = 0  # Initialize score

print("What is the fastest dog breed?")
userAnswer = input().lower()  # Converts input to lowercase
if userAnswer == "greyhound":
    print("Correct!")
    score += 1
else:
    print("Incorrect, but it's okay!")

print("Which breed is known for its wrinkled face and blue-black tongue?")
userAnswer = input().lower()
if userAnswer == "chow chow":
    print("Correct!")
    score += 1
else:
    print("Incorrect, but it's okay!")

print("What is the most popular dog breed in the U.S.?")
userAnswer = input().lower()
if userAnswer == "labrador retriever":
    print("Correct!")
    score += 1
else:
    print("Incorrect, but it's okay!")

print("What sense is strongest in dogs?")
userAnswer = input().lower()
if userAnswer == "smell":
    print("Correct!")
    score += 1
else:
    print("Incorrect, but it's okay!")

print("How many toes does a dog usually have on each paw?")
userAnswer = input().lower()
if userAnswer == "4":
    print("Correct!")
    score += 1
else:
    print("Incorrect, but it's okay!")

# Display final score
print("🎉 You did it! Your final score is: {}/5 🎉".format(score))