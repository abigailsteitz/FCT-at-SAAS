print("Hello World!")
print("Welcome to my quiz about pop culture")

# Start the score at 0
score = 0

# Question 1
print("\nQ1: Who is the 'catch me outside' girl?")
print("a) Bhad Bhabie")
print("b) Alabama Barker")
print("c) Woah Vicky")
print("d) Lil Tay")
answer = input("Your answer: ")

if answer.lower() == "a":
    print("PERIODT 🔥")
    score += 1000
else:
    print("WRONG 😩")

# Question 2
print("\nQ2: Who said 'boyfriend I'm nervous'?")
print("a) Charli D'Amelio")
print("b) Addison Rae")
print("c) Nessa Barrett")
print("d) Dixie D'Amelio")
answer = input("Your answer: ")

if answer.lower() == "b":
    print("YASSS QUEEN 👑")
    score += 1000
else:
    print("NOPE 💀")

# Question 3
print("\nQ3: Who created Floptropica?")
print("a) jifaei")
print("b) Nicki Minaj")
print("c) what i do girl")
print("d) Gavin")
answer = input("Your answer: ")

if answer.lower() == "a":
    print("Correct! ICONIC ✨")
    score += 1000
else:
    print("Try again boo 💅")

# Question 4
print("\nQ4: Who's the most canceled on YouTube?")
print("a) Trisha Paytas")
print("b) Tana Mongeau")
print("c) Colleen Ballinger")
print("d) James Charles")
answer = input("Your answer: ")

if answer.lower() == "d":
    print("You ATE 😤")
    score += 1000
else:
    print("Not giving... ❌")

# Question 5
print("\nQ5: What's the most used app?")
print("a) Instagram")
print("b) Snapchat")
print("c) TikTok")
print("d) Facebook")
answer = input("Your answer: ")

if answer.lower() == "c":
    print("Slayyyy 🕺")
    score += 1000
else:
    print("Girl no 💔")

# Final score
print("\nYou scored", score, "points out of 5000!")

# Optional flair
if score == 5000:
    print("YOU ATE 💖💯🔥")
elif score >= 3000:
    print("Not bad, girl 🌟")
elif score > 0:
    print("You tried and flopped 😬")
else:
    print(" Are you even chronic?? 🤡")