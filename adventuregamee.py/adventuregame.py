import random
# Add a score variable at the start of the game
score = 0

print("Hi! Welcome to the Lebron adventure game!")

print("You run into Steph Curry on the street. Do you talk to him? a) yeah! b) nah bruh")
Talk = input().lower()

if Talk == "a":
    score += 10  # Award points for talking
    print("You talk with him...")
    
    print("Steph Curry averaged 30.1 points, 6.7 assists, and 5.4 rebounds. Do you tell him that he played well this season?")
    print("a) Yup")
    print("b) Nope")
    
    Review = input().lower()
    
    if Review == "a":
        score += 20  # Award points for complimenting
        print("Curry appreciates the support. He asks you if he deserved an MVP. a) Yes b) Nope")
        
        Compliment = input().lower()

        if Compliment == "a":
            score += 10  # Award points for being nice
            print("You're too nice. You lose.")
        
        elif Compliment == "b":
            score -= 10  # Deduct points for making Curry mad
            print("Curry is mad. He challenges you to a game of basketball. Do you accept? a) Yes b) No")
            
            Challenge = input().lower()

            if Challenge == "a":
                # Decide the outcome based on a die roll
                dice = random.randint(1, 6)
                print(f"You rolled a {dice}.")
                if dice % 2 == 0:  # Even roll means win
                    score += 30
                    print("You win! Nice!")
                else:  # Odd roll means lose
                    score -= 20
                    print("You lose!")
            elif Challenge == "b":
                score -= 20  # Deduct points for refusing
                print("You lose!")
            else:
                print("Not understood: " + Challenge)
        else:
            print("Not understood: " + Compliment)
    
    elif Review == "b":
        score -= 10  # Deduct points for undervaluing Curry
        print("Curry doesn't appreciate being undervalued. He challenges you to a basketball game. Do you agree to play? a) Yes b) No")
        
        Challenge = input().lower()
        if Challenge == "a":
            # Decide the outcome based on a die roll
            dice = random.randint(1, 6)
            print(f"You rolled a {dice}.")
            if dice % 2 == 0:  # Even roll means win
                score += 30
                print("You play against Curry and win! Nice!")
            else:  # Odd roll means lose
                score -= 20
                print("You lose!")
        elif Challenge == "b":
            score -= 20  # Deduct points for refusing
            print("You lose by default!")
        else:
            print("Not understood: " + Challenge)
    else:
        print("Not understood: " + Review)

elif Talk == "b":
    score -= 10  # Deduct points for being antisocial
    print("Too antisocial. You lose.")
else:
    print("Not understood: " + Talk)

# Display the final score
print(f"Your final score is: {score}")