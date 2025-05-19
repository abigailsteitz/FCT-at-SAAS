
print("You are a native to Terror land, a place ruled by an evil robot queen.")
print("For the past couple of years, you have been involved with the Rebels")
print("Now the time has come, you have been chosen to go to the palace and defeat the queen, once and for all.")
print("Before you leave, there are some things you have to do")
  


#computer chosses a rondom nuber to determine the players partner
import random
if random.randint(1, 4) == 1:
    partner = "Aggie"
    print("  ")
    print("You embark with Aggie, the blacksmith")
elif random.randint(1, 4) == 2:
    partner = "Steve"
    print("  ")
    print("You embark with Steve, the traveler")
elif random.randint(1, 4) == 3:
    partner = "Burt"
    print("  ")
    print("You embark with Burt, the rebel spy")
elif random.randint(1, 4) == 4:
    print("  ")
    print("You go out alone.")
    partner = "none"
else:
    print("  ")
    print("You go out alone.")
    partner = "none"

    
print("  ")
print("  ")
print("Next, what weapon would you like for protection?")
print("1. Sword")
print("2. Bow")
print("3. Axe")
print("4. Baseball Bat")
if partner == "Aggie":
    print("  ")
    print("Aggie suggests taking the bow.")
else: 
    print("  ")
userAnswer = input(" ")

if userAnswer == "1":
   print("  ")
   print("You have chosen the sword.")
   weapon = "sword"
    
elif userAnswer == "2":
    print("  ")
    print("You have chosen the bow.")
    weapon = "bow"
elif userAnswer == "3":
    print("  ")
    print("You have chosen the axe.")
    weapon = "axe"
elif userAnswer == "4":
    print("  ")
    print("You have chosen the baseball bat.")
    weapon = "baseball bat"
else:
    print("  ")
    print("Invalid choice. Please select a valid option.")

print("  ")
print("  ")
print("ok, now, what path would you like to take?")
print("A: the desert path")
print("B: the forest path")
print("C: the hill path")

if partner == "Steve":
    print("  ")
    print("Steve suggests taking the desert path.")
elif partner == "Burt":
    print("  ")
    print("Burt suggests taking the hill path.")
elif partner == "Aggie":
    print("   ")
elif partner == "none":
    print("You have no partner to ask for advice.")
else: 
    print("Invalid choice, please try again")
choice = input(" ")

if choice == "A":
    print("  ")
    print("you chose the desert path")
    path = "desert"
elif choice == "B":
    print("  ")
    print("you chose the forest path")
    path = "forest"
elif choice == "C":
    print("  ")
    print("You chose the hill path")
    path = "hill"
else:
    print("Invalid choice. Please restart the game and choose a valid option.")

if path == "hill":
    print("   ")
    print("You get robbed and lose all your weapons.")
    weapon = "none"
    gold = 0

elif path == "forest":
    print("  ")
    print("your partener gets eaten by a bear, but you make it to the palace.")
    partner = "none"
    gold = 0
    
elif path == "desert":
    print("  ")
    print("you and your partner find gold along the way.")
    gold = 100

else:
    print("  ") 
    print("Invalid choice. Please select a valid option.")

print("  ")
print("you have made it to the palace. Now you must get past the moth gaurds.")
print("  ")
print("do you want to:")
print("A: fight them")
print("B: sneak past them")
print("C: bribe them")
userAnswer = input(" ")

if userAnswer == "A":
    if weapon == "sword":
        print("  ")
        print("The sword is too heavy to throw, so the guards fly around you and arrest you.")
        print("You lose.")
        make = False
    elif weapon == "bow":
        print("  ")
        print("You shoot the guard with the bow and arrow, and the guard dies.")
        make = True
    elif weapon == "axe":
        print("  ")
        print("You throw the axe at the guard, and the guard dies.")
        print("But, the axe breaks, and you have no weapon.")
        weapon = "none"
        make = True
    elif weapon == "baseball bat":
        print("  ")
        print("You hold the bat up to the moths, and since it is made of cedar, the guards are scared and let you pass through.")
        make = True
    elif weapon == "none":
        print("  ")
        print("You have no weapons, so you fight hand to hand. However, the gaurds have weapons, and easily kill you.")
        print("You lose.")
        make = False
    else:
        print("  ")
        print("Invalid weapon choice. You lose.")
        make = False
elif userAnswer == "B":
    if partner == "none":
        print("  ")
        print("Since you are alone, you are able to successfully sneak past the guards.")
        make = True
    elif partner == "Aggie":
        print("  ")
        print("Aggie is too loud, and the guards catch you.")
        print("You lose.")
        make = False
    elif partner == "Steve":
        print("  ")
        print("Steve gets caught and he has your weapons. You successfully make it through though, but now you have no weapons.")
        weapon = "none"
        make = True
    elif partner == "Burt":
        print("  ")
        print("Uh Oh! Burt is actually a double agent and rats you out to the guards.")
        print("You lose.")
        make = False
    else:
        print("  ")
        print("Invalid partner choice. You lose.")
        make = False

elif userAnswer == "C":
    if gold == 100:
        print("  ")
        print("You bribe the gaurds with gold, and they let you pass.")
        make = True
        gold = 0
    elif gold == 0:
        print("  ")
        print("You have no gold to bribe the guards with. You lose.")
        make = False
    else:
      print("  ")
      print("Invalid choice. Please restart and try again")
      make = False

if make == True:
    print("  ")
    print("You have made it to the palace.")
    print("Congratulations!")
    print("  ")
    print("However, you have to defeat the evil robot queen in order to free the land")
    print("  ")
    print("To defeat the queen, would you like to:")
    print("A: fight her")
    print("B: Ask her a math problem")
    print("C: become an inside man")
    userAnswer = input(" ")
    
    if userAnswer == "A":
        print("  ")
        print("You have chosen to fight the queen.")

        if weapon == "sword":
            print("  ")
            print("a sword")
            print("You swing your sword at the queen, but since she is made of metal she takes no damage.")
            print("You lose.")
            make = False
        elif weapon == "bow":
            print("  ")
            print("a bow")
            print("You shoot the queen with your bow and arrow, but miss.")
            print("You lose.")
            make = False
        elif weapon == "axe":
            print("  ")
            print("an axe")
            print("You throw the axe at the queen, and it hits her circuit board and kills her.")
            print("You win!")
            make = True
        elif weapon == "baseball bat":
            print("  ")
            print("a baseball bat")
            print("You swing the bat at the queen, but it breaks.")
            print("You lose.")
            make = False
        elif weapon == "none":
            print("  ")
            print("You have no weapons, so you fight hand to hand. However, the gaurds have weapons, and easily kill you.")
            print("You lose.")
            make = False
    elif userAnswer == "B":
        print("  ")
        print("You have chosen to ask the queen a math problem.")
        print("What problem would you like to ask her?")
        print("  ")
        print("A: 2 + 2")
        print("B: 179 + 2245 * 3335")
        print("C: 0^2")
        userAnswer = input(" ")
        if userAnswer == "A":
            print("The queen easily solves the math problem and kills you.")
            make = False
        elif userAnswer == "B":
            print("The queen easily solves the math problem and kills you.")
            make = False
        elif userAnswer == "C":
            print("The queen is confused by the math problem and you win!")
            make = True
        else:
            print("Invalid math problem. You lose.")
            make = False
    elif userAnswer == "C":
        print("You have chosen to become an inside man.")
        print("You tell the queen that you are a spy and you want to join her.")
        print("She believes you and lets you in.")
        print("However, she figures out you are a double agent and kills you.")
        make = False

if make == True:
    print("You have defeated the evil robot queen and freed the land.")
    print("Congratulations!")  

if make == False:
    print("You have lost the game.")
    print("Please restart the game and try again.")