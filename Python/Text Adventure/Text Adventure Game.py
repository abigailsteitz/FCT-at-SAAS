import random
def finalBattle():
  print("Do you do a) stab him with your sword or b) try to hit him in the head")
  battle = input()

  if battle == "a":
    print("you run towards him and stab him with your sword and destroy him")
    print("you win nice!")
  else:
    print("you try to hit him in the head but he dodges and destroys you with his sword")
    print("You lose!")

print("Hi! Welcome to Ocean Adventure Game")
print("You find 2 random fish and they both say that they know where the sharks base is but also not to trust each other")
print("You ask them if they can take you to the sharks base")
randomnumber = random.randint(1, 10)
print("'A dice [1-10] is rolled to see if the fish agree to help you'")
print("If the number is 5 or higher, they agree to help you")
print("The number is: " + str(randomnumber))
if randomnumber >= 5:
  print("The fish agree to help you!")
  print("Do you want to a) trust fish a or b) go with fish b")
  fishtrust1 = input()
else:
  print("The fish do not agree to help you!")
  print("You lose!")
  exit()
if fishtrust1 == "b":
  print("You have chosen fish b and he takes you to the sharks base")
  
  print("you smell someting good, do you a) follow the smell or b) keep going inside the base.")

  
  smellchoice = input()
  
  if smellchoice == "b":
    print("you made it into the base!")
    print("You see a giant shark and he is holding a sword, you have to fight him!")
    print("Do you want to a) swim towards him or b) chicken out and run away")
    swimtowards = input()
    if swimtowards == "a":
      print("you swim towards him and he is not happy, you have to fight him!")
      print("you reach in your backpack and find a mystery sword and a normal sword")
      print("Do you want to a) use the mystery sword or b) use the normal sword")
      swordchoice = input()
      if swordchoice == "a":
        print("you have chosen the mystery sword")
        print("you walk up to the shark and pull out the mystery sword!")
        finalBattle()
      if swordchoice == "b":
        print("you have chosen the normal sword")
        print("you walk up to the shark and pull out the normal sword!")
        print("You run at the shark and try to stab him with the sword but it breaks")
        print("The shark then pulls out a giant sword and destroys you!")
        print("You lose!")
    else:
      print("you run away!")
      print("You lose!")
        
    
    
  elif smellchoice == "b":
    print("you follow the smell and it leads you to a giant shark!")
    print("Do you a) try to fight him or b) run away")
    fightchoice = input()
    if fightchoice == "a":
      print("you lose!")
    if fightchoice == "b":
      print("you lose!")
  else:
    print("not successful, go home")
elif fishtrust1 == "a":
  print("fish a takes you to some random place and you get lost, you lose")
else:
  print("Not understood: " + fishtrust1)