file = open ("Python/Text Adventure/jeppydata.csv")

data = file.read().splitlines()

import time


      
print("While walking through the woods, you see a curious little hat pokingout of a bush.")

print("The little hat moves towards you, and a miniscul gnome glares up at you.")

time.sleep(2)

print("He says 'Aha, there you are! I have been looking for you!'")

print("'I am short gerAld, the gnome. I need your help to fight the giant Jeppyfish - but I also need your help to free my friend - Tall Gerald.'")

time.sleep(2)

print("'Before you fight Jeppyfish, you'll need to find a buddy to help you. The buddies are at the helper shelter.'")

print("Will you go find tall gerAld, or go to the helper shelter to get allies in our fight?")

party = ["shortGerald"]

# if "tallGerald" in party:
#     print("You have tall Gerald in your party.")

time.sleep(2)
print("1. Go to the helper shelter")
print("2. Find tall gerAld")
choice = input("Enter your choice (1 or 2): ")
if choice == "1":
    print("what about my friend... let's go to the helper shelter i guess")
elif choice == "2":
    print("you have found tall gerAld! [he is now in your party]")
    print("Hello, i am tall gerAld. i am a tall gnome. I will help you fight the jeppyfish in return for your kindness.")

    party.append("tallGerald")
    print(party)
else:
    print("no, you have to help me you dont get a choice")

time.sleep(2)
print("After hours of walking, you finally get to the edge of the forest. You see a small and ramshackle hut, seemingly abandoned, but short gerAld says this is the place.")

time.sleep(2)
#install an image
from PIL import Image
img = Image.open("Python/Text Adventure/shack.jpg")
img.show()

time.sleep(2)

print("You walk into the helper shelter, which isn't much of a shelter at all.")
print("You notice a few small creatures lounging around.")

time.sleep(2)

print("There are 2 penguins admiring a bonzi tree.")
print("A pathetic looking fish swimming in a tank - all wearing tiny top hats and bows;")
print("Finally, huddled in the corner is a small lump of hair that is shaking. You have no idea what kind of creature it is.")

time.sleep(2)

print("Small gerAld says,'we only have three of our helpers in now, but they are the best in the kindgom, lucky of you. The first are forest penguins, the second ar fancy fish, and the third - we call him Crazy Jim.")
print("You can pick one creature to help you fight Jeppyfish. Who will you pick?")

time.sleep(2)

print("1. Forest penguins")
print("2. Fancy fish")
print("3. Crazy Jim")
choice = input("Enter your choice (1 or 2 or 3): ")
if choice == "1":
    print("You have chosen the forrest penguin brothers, Crisco and Pascal. They will now help you fight the jeppyfish.")
    time.sleep(2)
    print("Hello, we are Crisco and Pascal. we are forest penguins. we will help you fight in exchange for food.")
    party.append("forest penguins")
    print(party)
elif choice == "2":
    print("You have chosen the fancy fish, who is swimming in a tank. he will now help you fight the jeppyfish.")
    time.sleep(2)
    print("Hello, I am a fancy fish. it is very nice to meet you indeed")
    party.append("fancy fish")
    print(party)
elif choice == "3":
    print("You have chosen Crazy Jim, He will now help you fight the jeppyfish.")
    print("The ball of hair stand up and turns around, revealing he is a very discheveled possum. You notice the shovel he's holding the fact that his eyes are looking in two different directions.")
    time.sleep(2)
    print("He says'Hello, I am Crazy Jim. You where right to choose me, MUHAHAHAHA!")
    party.append("crazy jim")
    print(party)
else:
    print("ummm theres only 3 choices")

print("You have chosen your helper. Now you must go to the Jeppyfish lair.")
time.sleep(2)
print("You slowly approch the dark cave at the edge of the beach, descending down into the ocean.")
print("As an expert swimmer and descedent of a mermaid, you're able to hold your breath and swim down into the heart of the lair eith ease.")
time.sleep(2)
print("Before you is the legandary Jeppyfish - a giant jellyfish with an orange-pink gradient color and a soft glow of yellow light.")
print("While the jeppyfish is usually a kind creature, this one is hostile because 2 months ago his boba was stolen. Ever since, he has been terrorizing the forest.")
time.sleep(2)
print("You must fight the Jeppyfish to save the forest!")
print("this is where i leave you, small gerAld says.")
time.sleep(2)
if "crazy jim" in party:
    print("crazy jim is struggling slighly in the water, but seems fine.")
if "fancy fish" in party:
    print("fancy fish is very happy to be in the water, and is swimming around in circles.")
if "forest penguins" in party:
    print("the forest penguins seemingly enjoying the water, but due to their forestyness,they are not very fast swimmers.")
print ("You are now in the Jeppyfish lair. beware!!")
time.sleep(2)
print("As you rount the corner, you see the beast. it is a ginourmous jellyfish, with poisonous orange and pink tentacles. as you approach, it turns and sees you!")
print("The Jeppyfish is angry! get ready to fight!:")

playerscore = 100
jeppyscore=100

while playerscore > 0 and jeppyscore > 0:
    print("Your current health:", playerscore)
    print("Jeppyfish's current health:", jeppyscore)
    time.sleep(2)

    print("What will you do?")
    print("1. Use your helper")
    print("2. Use your fists")
    if "tallGerAld" in party:
        print("3. Use tall gerAld")

    choice = input("Enter your choice (1 or 2 or 3): ")
    if choice == "1":
        import random
        random_integer = random.randint(10, 20)
        jeppyscore = jeppyscore - random_integer
    elif choice == "2":
        import random
        random_integer = random.randint(5, 15)
        jeppyscore = jeppyscore - random_integer
        print("Jeppyfish's current health:", jeppyscore)
    elif choice == "3":
        import random
        random_integer = random.randint(10, 20)
        playerscore = playerscore + random_integer
        print("Jeppyfish's current health:", jeppyscore)
    else:
        print("Invalid choice. Please try again.")
        continue
    jeppyattack = random.randint(5, 15)
    playerscore = playerscore - jeppyattack
    print("Jeppyfish attacks you! Your current health:", playerscore)

if playerscore <= 0:
    print("You have been defeated by the Jeppyfish! You buddies abandon you and the Jeppyfish puts you in its next boba drink. Play again to win.")
elif jeppyscore <= 0:
    print("You defeated the Jeppyfish! It shrinks to the size of a noraml Jellyfih. It looks up at you with large boba eyes.")
    print("The Jeppyfish says, 'You calmed me down, thank you.'")
    time.sleep(2)
    print("You, your buddies, and the Jeppyfish all swim into the sunset and go get boba.")
    print("Thank you for playing!")