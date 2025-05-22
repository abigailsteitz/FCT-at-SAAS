score = 0
print("Welcome to the Medieval Text Adventure Game! Your objective is to steal the King's crown. Which character would you like to choose?")
print("(type a, b, c, etc...)")
print("a) Witch")
print("b) Knight")
print("c) Hunter")
print("d) Merchant")
print("e) Peasant")
print("f) Random!!")
useranswer1 = input()
print(useranswer1)
print(" ")

if useranswer1 == "f" :
    print("Congrats! You're going to get a radom character! Let's see what you get...")
    import random
    characters = ["Witch", "Knight", "Hunter", "Merchant", "Peasant"]
    random_character = random.choice(characters)
    print("You got a " + random_character + "! Let's see what your health bar starts at...")

    match random_character:
        case "Witch":
            score = 200
        case "Knight":
            score = 150
        case "Hunter":
            score = 150
        case "Merchant":
            score = 150
        case "Peasant":
            score = 50

    print(f"(your health is at: {score} out of 200)")
    print("Which setting do you want to start in?")
    print("a) The Swamp")
    print("b) The Village")
    print("c) The Royal Grounds")
    useranswer2 = input()
    print(useranswer2)  

if useranswer1 == "a" :
    print("Great choice!! You've chosen to be a Witch, the most powerful player! Your health bar starts full! Here's your next choice...")
    score = score + 200
    print("(your health is at: " + str(score) + " out of 200)")
    print (" ")
    print("Which setting do you want to start in?")
    print("a) The Swamp")
    print("b) The Village")
    print("c) The Royal Grounds")
    useranswer2 = input()
    print(useranswer2)    

if useranswer1 == "b" :
    print("Incredible choice!! You've chosen to be a Knight. Your health bar starts at 150! Here's your next choice...")
    score = score + 150
    print("(your health is at: " + str(score) + " out of 200)")
    print (" ")
    print("Which setting do you want to start in?")
    print("a) The Swamp")
    print("b) The Village")
    print("c) The Royal Grounds")
    useranswer2 = input()
    print(useranswer2)

if useranswer1 == "c" :
    print("Nice choice!! You've chosen to be a Hunter. Your health bar starts at 150! Here's your next choice...")
    score = score + 150
    print("(your health is at: " + str(score) + " out of 200)")
    print (" ")
    print("Which setting do you want to start in?")
    print("a) The Swamp")
    print("b) The Village")
    print("c) The Royal Ground")
    useranswer2 = input()
    print(useranswer2)

if useranswer1 == "d" :
    print("Good choice!! You've chosen to be a Merchant. Your health bar starts at 150!. Here's your next choice...")
    score = score + 150
    print("(your health is at: " + str(score) + " out of 200)")
    print (" ")
    print("Which setting do you want to start in?")
    print("a) The Swamp")
    print("b) The Village")
    print("c) The Royal Grounds")
    useranswer2 = input()
    print(useranswer2)

if useranswer1 == "e" :

    print("Interesting choice!! You've chosen to be a Peasant. Your health bar starts at 50! Here's your next choice...")
    score = score + 50
    print("(your health is at: " + str(score) + " out of 200)")
    print (" ")
    print("Which setting do you want to start in?")
    print("a) The Swamp")
    print("b) The Village")
    print("c) The Royal Grounds")
    useranswer2 = input()
    print(useranswer2)

#SWAMP
if useranswer2 == "a" :
    print(" ")
    print("You find yourself in a Swamp at dusk, next to a large fallen tree.")
    print("On your left, you see a small, lit up wooden cabin. On your right, a staight path to an open feild through the trees. What do you choose?")
    score = score
    print("(your health is at: " + str(score) + " out of 200)")
    print(" ")
    print("a) You go left, to the faintly lit cabin. Maybe you'll find something or someone useful to your journey to the palace to steal the crown.")
    print("b) You go right, to the open path to explore the quick way to the palace. The quicker you get to the crown, the better.")
    useranswer31 = input()
    print(useranswer31)
    print(" ")

    if useranswer31 == "a" :
        print("You walk into the cabin, and bump into a theif rummaging through the cabin's chests! Do you...")
        score = score
        print("(your health is at: " + str(score) + " out of 200)")
        print(" ")
        print("a) Try to fight him! He might hurt me or steal my belongings!")
        print("b) Apologize for intruding and try to have a conversation with him. Who knows, maybe you might make a friend?")
        useranswer41 = input()
        print(useranswer41)
        print(" ")

        if useranswer41 == "a":
            print("You raise your weapon and attack! The thief is startled, but fights back fiercely.")
            print("After a rough brawl, you manage to defeat him, but not without injury.")
            score -= 25
            print("You loot a mysterious map from his pocket before leaving.")
            print("(you lost -25 health but gained a palace map!)")
            print("(your health is now: " + str(score) + " out of 200)")
            print(" ")
            print("What do you do with the palace map?")
            print("a) Use the map to sneak into the palace through the underground tunnels.")
            print("b) Sell the map to a group of bandits in exchange for food and weapons.")
            useranswer51 = input()
            print(useranswer51)
            print(" ")
            
            if useranswer51 == "a":
                print("Using the map, you quietly navigate a tunnel system leading right beneath the palace walls. You emerge inside the palace kitchen, undetected.")
                score += 30
                print("(you gained +30 health for avoiding danger!)")
                print("(your health is now: " + str(score) + " out of 200)")

            if useranswer51 == "b":
                print("You meet a group of bandits in the forest and trade the map for two pieces of bread and a dagger. Not bad!")
                score += 20
                print("(you gained +20 health from the food and weapon!)")
                print("(your health is now: " + str(score) + " out of 200)")

        if useranswer41 == "b":
            print("You apologize and back away, hands raised. The thief pauses... then smiles.")
            print("'Didn't expect manners in the swamp,' he says. You talk for a bit, and he gives you advice on secret palace entrances.")
            score += 10
            print("(you made a connection and gained +10 health!)")
            print("(your health is now: " + str(score) + " out of 200)")
            print(" ")

            print("How do you want to proceed?")
            print("a) Ask the thief to come with you as an ally on your mission.")
            print("b) Continue your journey solo, using his advice to sneak in through the sewage pipes.")
            useranswer52 = input()
            print(useranswer52)
            if useranswer52 == "a":
                print("The thief agrees to join you. He's sneaky and skilled with locks. Could be useful!")
                score += 25
                print("(you gained +25 health with your new ally!)")
                print("(your health is now: " + str(score) + " out of 200)")
                print(" ")
            
            if useranswer52 == "b":
                print("You part ways, but the thief's tip helps you slip through the sewage pipes straight into the palace courtyard.")
                score += 15
                print("(you gained +15 health from successfully infiltrating solo!)")
                print("(your health is now: " + str(score) + " out of 200)")
                print(" ")

    if useranswer31 == "b" :
        print("You start on the path to the palace... After a long night of walking and no rest, you lose 10 health points!!") 
        print("Oh no! At least you see the palace in the distance! Do you...")
        score -= 10
        print("(your health is at: " + str(score) + " out of 200)")
        print(" ")
        print("a) Hitch a ride on a passing cavalier's horse. You're tired...")
        print("b) Pick up the pace and start jogging to the palace. You need to sneak into the palace before the sun rises!")
        useranswer42 = input()
        print(useranswer42)
        print(" ")

        if useranswer42 == "a":
            print("You wave down the cavalier, pretending to be a royal messenger.")
            print("He's suspicious but lets you on. You hop on the horse and ride fast toward the palace.")
            print("Unfortunately, he realizes you're lying and throws you off near the gates.")
            score -= 20
            print("(you lost 20 health from the fall but made it close to the palace!)")
            print("(your health is now: " + str(score) + " out of 200)")
            print("You're now at the palace perimeter... bruised but close.")
            print(" ")
            print("Now at the gates, what do you do?")
            print("a) Sneak into the palace stables while the guards are distracted.")
            print("b) Hide in a cart headed into the castle with the morning delivery.")
            useranswer53 = input()
            print(useranswer53)
            print(" ")
            if useranswer53 == "a":
                print("You dart into the stables and hide behind hay bales. When the guards leave, you slip into the palace.")
                score += 20
                print(" ")
                print("(you gained +20 health for stealth and positioning!)")
                print("(your health is now: " + str(score) + " out of 200)")

            if useranswer53 == "b":
                print("You tuck yourself into a delivery cart. Hours later, you're wheeled right into the palace storeroom.")
                score += 15
                print(" ")
                print("(you gained +15 health for clever infiltration!)")
                print("(your health is now: " + str(score) + " out of 200)")

        if useranswer42 == "b":
            print("You push yourself to run. You're exhausted but determined.")
            print("Just before sunrise, you arrive at the palace gates and hide in the bushes to rest.")
            score -= 10
            print("(you lost 10 health from exhaustion)")
            print("(your health is now: " + str(score) + " out of 200)")
            print("You spot a guard dozing off by a side entrance... could be your way in.")
            print(" ")
            print("You rest for a moment and consider your next move...")
            print("a) Climb the ivy up the palace wall to enter through a high window.")
            print("b) Follow a sleepy servant through a service entrance left ajar.")
            useranswer54 = input()
            print(useranswer54)
            print("")

            if useranswer54 == "a":
                print("You climb the ivy carefully, reach a high window, and slip inside undetected.")
                score += 20
                print("(you gained +20 health for the risky but stealthy approach!)")
                print("(your health is now: " + str(score) + " out of 200)")

            if useranswer54 == "b":
                print("You shadow the servant into the palace. No one notices you as the door swings shut.")
                score += 25
                print("(you gained +25 health for perfect timing!)")
                print("(your health is now: " + str(score) + " out of 200)")


#VILLAGE
if useranswer2 == "b" :
    print(" ")
    print("You find yourself in a humble Village at noon, near the communal village well, and see a necklace on the floor. You pick it up and pocket it.")
    print("On your left, you see a stable filled with horses. On your right, an old lady crying by the well. What do you choose?")
    score = score
    print("(your health is at: " + str(score) + " out of 200)")
    print(" ")
    print("a) You go left, to the horse stable. Maybe you can sneak away with a horse without anyone noticing...")
    print("b) You go right, towards the upset old lady. You want to figure out what's wrong!")
    useranswer32 = input()
    print(useranswer32)
    print(" ")
    
    if useranswer32 == "a" :
        print("You stealthily make your way into the stable and see dozens of horses...")
        print("You spot a well cared for looking horse, and read the plaque on its' stall:")
        print("'Maximus, prize horse. #1 in Rivertown annual race.' Do you...")
        score = score
        print("(your health is at: " + str(score) + " out of 200)")
        print(" ")
        print("a) Take the prize horse and get out of here! He's the fastest, nobody will catch you.")
        print("b) Take one of the other horses. Someone will notice the prize horse missing...")
        useranswer33 = input()
        print(useranswer33)
        print(" ")

        if useranswer33 == "a":
            print("You gallop away on Maximus! But... a rider spots you and raises the alarm. You're now being hunted!")
            score -= 30
            print("(your health is at: " + str(score) + " out of 200)")
            print(" ")
            print("What do you do now that you're being hunted?")
            print("a) Ride toward the palace at full speed, dodging patrols.")
            print("b) Abandon the horse and sneak into the woods to hide.")
            useranswer55 = input()
            print(useranswer55)
            print(" ")
            if useranswer55 == "a":
                print("You ride full speed, dodging arrows and guards. You're nearly hit, but arrive at the palace gate.")
                score += 10
                print("(you gained +10 health for boldness!)")
                print("(your health is at: " + str(score) + " out of 200)")

            if useranswer55 == "b":
                print("You abandon Maximus in the woods and sneak through a creek. You're safe but soaked and cold.")
                score -= 5
                print("(you lost -5 health from exposure but avoided patrols.)")
                print("(your health is at: " + str(score) + " out of 200)")

        if useranswer33 == "b":
            print("Smart move. You quietly slip out with a plain brown horse and head off unnoticed.")
            score = score
            print("(your health is at: " + str(score) + " out of 200)")
            print(" ")
            print("Where do you head on the horse?")
            print("a) Stop at a tavern on the way to gather intel about the palace.")
            print("b) Take a quiet back road to avoid attention and save energy.")
            useranswer56 = input()
            print(useranswer56)
            print(" ")
            if useranswer56 == "a":
                print("At the tavern, a bard shares gossip about a hidden door used by staff.")
                score += 15
                print("(you gained +15 health for valuable intel!)")
                print("(your health is at: " + str(score) + " out of 200)")

            if useranswer56 == "b":
                print("You take the back road. It's uneventful but long. You tire out.")
                score -= 10
                print("(you lost -10 health from fatigue but arrived unseen.)")
                print("(your health is at: " + str(score) + " out of 200)")

        

    if useranswer32 == "b" :
        print("You walk towards the old lady. She explains that lost her favorite necklace.")
        score = score
        print("(your health is at: " + str(score) + " out of 200)")
        print(" ")
        print("a) You offer her the necklace you found earlier! You don't need it, any she'll be so happy to get it back!")
        print("b) You walk away, it's not your problem. Finders, keepers.")

        useranswer34 = input()
        print(useranswer34)
        print(" ")

        if useranswer34 == "a":
            print("The old lady gasps as you hand her the necklace.")
            print("'This is it!' she cries. 'Bless your heart!'")
            print("She gives you a tight hug and whispers a spell... suddenly, a small glowing orb floats into your bag.")
            print("You've gained a Potion of Invisibility!")
            score += 20
            print(" ")
            print("(you gained +20 health for your kindness and received a Potion of Invisibility!)")
            print("(your health is now: " + str(score) + " out of 200)")
            print(" ")
            print("How do you want to use your new advantage?")
            print("a) Use the Invisibility Potion to slip into the palace undetected.")
            print("b) Visit the old lady's hut... she offers to teleport you to the palace gate.")
            useranswer57 = input()
            print(useranswer57)
            print(" ")
            if useranswer57 == "a":
                print("You use the Invisibility Potion and walk right past the royal guards.")
                score += 30
                print("(you gained +30 health for perfect use of magic!)")
                print("(your health is at: " + str(score) + " out of 200)")

            if useranswer57 == "b":
                print("You accept teleportation. You land safely but a little dizzy at the palace garden.")
                score += 10
                print("(you gained +10 health, slight nausea but no harm.)")
                print("(your health is at: " + str(score) + " out of 200)")

        if useranswer34 == "b":
            print("You shrug and walk away, clutching the necklace. It sparkles in your hand.")
            print("Suddenly, a loud yell comes from behind... the town guards accuse you of theft!")
            print("You run, dodging through the crowd, but not before taking a hit from a thrown rock.")
            score -= 30
            print(" ")
            print("(you lost -30 health from the escape and are now being watched in the village.)")
            print("(your health is now: " + str(score) + " out of 200)")
            print(" ")
            print("You examine the necklace while hiding. It begins to glow...")
            print("a) Hide in a barn until nightfall, then make your way to the palace.")
            print("b) Use the necklace's magic (revealed now) to disguise yourself as a noble.")
            useranswer58 = input()
            print(useranswer58)
            print(" ")
            if useranswer58 == "a":
                print("You hide in a barn, but hay mites bite you overnight. Ouch.")
                score -= 10
                print("(you lost -10 health but avoided suspicion.)")
                print("(your health is at: " + str(score) + " out of 200)")

            if useranswer58 == "b":
                print("The necklace disguises you as nobility. You blend in and even get offered tea by a butler.")
                score += 25
                print("(you gained +25 health for brilliant deception!)")
                print("(your health is at: " + str(score) + " out of 200)")


#PALACE
if useranswer2 == "c" :
    print("You cheater. You can't just skip to the easy part. Try again.")
