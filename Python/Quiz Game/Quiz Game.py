print("Hello")
print("Welcome to Alice's and Sabra's Teen Culture Quiz!")

score = 0  # Initializing score

# Question 1
print("Which actor is known for playing Thor in the Marvel movies?")
print("(a) Chris Pine")
print("(b) Chris Evans")
print("(c) Chris Hemsworth")
print("(d) Chris Pratt")

useranswer = input()

if useranswer in ["chris hemsworth", "c"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
print("What sport did Noah Beck play before becoming an influencer?")
print("(a) Basketball")
print("(b) Baseball")
print("(c) Football")
print("(d) Soccer")

useranswer = input()

if useranswer in ["soccer", "d"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
print("Which of these is an absolute red flag?")
print("(a) People who bite ice cream with their front teeth")
print("(b) People who text 'K.'")
print("(c) People who don’t like dogs")
print("(d) People who say 'pineapple belongs on pizza' with TOO much confidence")

useranswer = input()

if useranswer in ["people who bite ice cream with their front teeth", "a"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 4
print("Which cast member is Drew Starkey rumored to be close friends with in real life?")
print("(a) Chase Stokes")
print("(b) Madison Bailey")
print("(c) Rudy Pankow")
print("(d) Madelyn Cline")

useranswer = input()

if useranswer in ["rudy pankow", "c"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 5
print("Which song by Doechii has recently gone viral on TikTok, inspiring dance challenges and lip-syncs?")
print("(a) Crazy")
print("(b) Anxiety")
print("(c) What It Is")
print("(d) Act Bad")

useranswer = input()

if useranswer in ["anxiety", "b"]:
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Final Score
print("The quiz is over! You got " + str(score) + " out of 5 correct")

# Score-based message
if score == 5:
    print("ate the whole plate! literally")
elif score >= 3:
    print("Not bad! You know your stuff.")
else:
    print("Oof... time to scroll TikTok more.")