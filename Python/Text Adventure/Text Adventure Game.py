print("Welcome to Pig Farm")

score = 0 

print("would you like to buy some pigs? yes or no?")
doyouwanttobuypigs = input()

if doyouwanttobuypigs == "no":
    print("you lose")
    score = 0
else:
    print("you're great!")
    print("nice job!")
    score += 1 

    print("buy food for your pigs? yes or no?")
    doyouwanttobuyfood = input()

    if doyouwanttobuyfood == "no":
        print("your pigs starved and died!")
    else:
        print("your pigs are nourished!")
        score += 1  

    print("do you want to buy a girl and boy pig? yes or no?")
    girlandboy = input()

    if girlandboy == "yes":
        print("YAY! More pigs!")
        print("nice job!")
        score += 1 
    else:
        print("no more pigs.")
    
    print("do you want to buy more fence? yes or no?")
    fencewant = input()
import random

fences = random.randint(1, 5) 
print(f"You have received {fences} fences!")

if fencewant == "yes":
        print("YAY! Your pigs thrive!")
        print("nice job!")
        score += 1  
else:
        print("your pigs escaped!")
    

print("do you want to sell half of your pigs? yes or no?")
sellpigs = input()

if sellpigs == "yes":
        print("you get money and win!")
        score += 1  
else:
        print("you went bankrupt and lost.")

print("the end.")
print(f"you got {score} out of 5.")
