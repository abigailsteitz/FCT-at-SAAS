# A very dangourous day at school

character = 0
print("")
print("Welcome to school!")
print("")
print("The progress you make relies on your character and the results of your choices.")
print("")
print("Choose your character.")
print("")
print("1. Lily: Lily is charasmatic and strong yet quite clumsy. Lily is reckless and can play soccer. She also hates math.")
print("2. Fish: Fish has an interesting point of view and can make friends with anyone. Fish is chaotic. Also fish is better")
print("3. Elsa: Calm, collected, and smart, but also very quiet. She is quick on her feet, but has weak arms because she is always reading.")
print("")

# Character Choice
firstuserAnswer = input()
if firstuserAnswer == "1" or firstuserAnswer.lower() == "Lily":
    print("")
    print("You are now Lily. You chose... poorly")
    character = "Lily"
    print("")  
elif firstuserAnswer == "2" or firstuserAnswer.lower() == "Fish":
    print("")
    print("You are now Fish. you chose... wisly")
    character = "Fish"
    print("")
elif firstuserAnswer == "3" or firstuserAnswer.lower() == "Elsa":
    print("")
    print("You are now Elsa. Yay!")
    character = "Elsa"
    print("")
else: 
    print("")
    print("That is not one of the characters. you will now recieve a random character.")
    print("")
    import random
    character = random.choice(["Lily", "Fish", "Elsa"])
    print("You are now " + character + ". Good luck!")
    print("")

# Choise one
print("You are midway through spring trimester, and it is another day at school like any other.")
print("On your way to class you remember that you have a math test today.")
print("You get a chill and get a bad feeling about something.")
print("")
print("You can either go to class and take your math test or skip class and miss it.")
print("")
print("What do you want to do?")
print("")
print("1. Go")
print("2. Skip")
print("")

# Go to class.
userAnswer = input()
if userAnswer == "1" or userAnswer.lower() == "go":
    print("")
    print("You decide to go to class. You walk into the classroom and sit down.")
    print("Almost imidiatly a stanger slowly enters the room. You can see they are holding a long jagged knife.")
    print("The fear is real.")
    print("")
    print("You have three options to try and make it out alive.")
    print("You can fight back by throwing the closest chair you can find, flee out the first floor window oppisit the door,")
    print("or you can freeze and stand there in fear.")
    print("")
    print("What do you do?")
    print("")
    print("1. Freeze.")
    print("2. Flight.")
    print("3. Fight.")
    print("")
    secondAnswer = input()

# Fight
if secondAnswer == "3" or secondAnswer.lower() == "fight":
    if character == "Lily":
        print("")
        print("You throw the chair at the approhing person as hard as you can.")
        print("The chair strikes them in the head, causing them to pass out, before they managed to hurt anyone.")
        print("Breathing heavaly you look around at your classmates. They are looking at you in admiring shock.")
        print("You are now the silently allected leader of the class.")
        print("")
        print("Now it is your job to figure out what to do next.")
        print("")
        print("You can either steal the attackers stuff or call athorities.")
        print("")
        print("1. Steal")
        print("2. Call")
        print("")
        userAnswerthree = input()

        while True:
            if userAnswerthree == "1" or userAnswerthree.lower() == "steal":
                print("")
                print("You dig through the attackers pockets and find a veriety of wepons not just the knife.")
                print("You distribute the wepons to you classmates.")
                print("You and your classmates discuss and deside to train with the wepons and becom a gang for justace and fight back agenst other attackers.")
                print("Your lives will be changed forever.")
                print("")
                print("If you do not like this ending feel free to try again.")
                print("")
                break
            elif userAnswerthree == "2" or userAnswerthree.lower() == "call":
                print("")
                print("You call the authorities and they arive shortly")
                print("They thank you, and request that you continue on with your day as usual.")
                print("Your teacher arrives and inministers the math test. You realize you don't understand anything on it.")
                print("")
                print("Dispite the heroics of the day you still fail your math test. Things really are just like they were before.")
                print("")
                print("If failing math tests are not your ideal happy ending then try again. Good luck!")
                print("")
                break
            else :
                print("")
                print("That was not one of the opptions. ")
                print("Your options are...")
                print("")
                print("1. Steal.")
                print("2. Call.")
                print("")
                userAnswerthree = input()

    if character == "ELsa":
        print("")
        print("You try to lift up the chair and throw it, but you lack the strength to do any damage.")
        print("The attacker dives for you and stabs you with the knife. ")
        print("You were a threat as soon as you tried to fight back.")
        print("")
        print("You are dead")
        print("")
        print("Your game has ended.")
        print("")
        print("...but all is not lost. You can try again. Good luck in your next life.")
        print("")

    if character == "Fish":
        print("")
        print("As you lift up the chair you here a crack and remember that you have a weak back.")
        print("The pain continues untill you can no longer stand.")
        print("As you vision goes black you see the attacker coming towards you.")
        print("... then nothingness.")
        print("")
        print("You have died.")
        print("")
        print("Instead of dieing in shame you can rise again.")
        print("Do you wish to die a hero?")
        print("")

# Flight
if secondAnswer == "2" or secondAnswer.lower() == "flight":
    if character == "Lily":
        print("")
        print("You wildly stand and run to the other side of the classroom trying to get out.")
        print("Unforchinitly in the panick you trip over a backpack and fall on your face.")
        print("Your nose hurts like fire. Blood and tears run down your face. The fear and pain causes you to black  out.")
        print("")
        print("Hours later you wake to find yourself in a hospital bed with a permintly twisted nose and a broken arm.")
        print("Could have been worse.")
        print("")
        print("Want to start your life over again without perminint ingeries?")
        print("")
        print("This could be a begining. Try again if it suits you.")
        print("")

    if character == "Elsa":
        print("")
        print("You hurridly stand up and bolt for the window, your heart beating wildly. Luckly you are a quick runner.")
        print("You make it to the window and shakily unlatch it.")
        print("Hopping out you quickly flatten yourself to the wall as a couple of people follow you out the window.")
        print("")
        print("You can wait outside the window to help others escaping, or you can keep running home.")
        print("")
        print("1. Stay.")
        print("2. Run.")
        print("")
        userAnswerfour = input()
        
        while True:
            if userAnswerfour == "1" or userAnswerfour.lower() == "stay":
                print("")
                print("You stay near the window and quiety listen to what is happening inside as you help your peers escape.")
                print("Before escaping yourself you overhere a phone call from the attacker.")
                print("Once you make it to the avacuation spot you are questioned by police and you share what you heard.")
                print("")
                print("Later in the week you get an Email from secret services asking to recruitment you after you get out of school.")
                print("You are now a secret agent.")
                print("Your career is now ashured.")
                print("")
                print("Wish to try again?")
                print("Go right ahead.")
                print("")
                break
            elif userAnswerfour == "2" or userAnswerfour.lower() == "run":
                print("")
                print("You run as fast as you can, not looking back, even as screams are heard behind you.")
                print("You run until you finaly make it home.")
                print("You have made it out safly.")
                print("")
                print("A couple hours later you get an angry phone call from the school complaining that you did not meet up at the avacuation spot.")
                print("You explain that you were not going to risk your life for a math test, but no luck.")
                print("You have lunch detention.")
                print("")
                print("Don't like this ending? Keep playing!")
                print("")
                break
            else:
                print("")
                print("That was not one of the opptions. ")
                print("Your options are...")
                print("")
                print("1. Stay.")
                print("2. Run.")
                print("")
                userAnswerfour = input()

    if character == "Fish":
        print("")
        print("You try to get up but your desk is right next to the door.")
        print("Your movement alerts the attacker and they scream as they charge right at you.")
        print("Your chair tips backwards and you fall, crying in fright.")
        print("The attacker jumps on top of your chest and stabs you repeatitly.")
        print("")
        print("Unsuprizingly after that you die.")
        print("")
        print("You should try again. That was just sad.")
        print("")

# Freeze
if secondAnswer == "1" or secondAnswer.lower() == "freeze":
    if character == "Lily":
        print("")
        print("Terror overcomes you and you freeze in place.")
        print("You watch as across the classroom the attacker killes your classmates.")
        print("Just when you think finaly got control over your body again you look up and find the attacker looming over you.")
        print("As you stare into their cruel eyes you do one last act of defiance and spit on their shoes.")
        print("The attackers eyes widen then narrow and that is the last thing you see as red takes over your mind and body.")
        print("")
        print("You have definitly died.")
        print("")
        print("Good job dieing like a reble while being frozen in fear. Try again and survive like a reble too!")
        print("")

    if character == "Elsa":
        print("")
        print("As the chaos begings you are jossled from all sides.")
        print("Though your brain is screeming at you to move or do something all you can do is stand there.")
        print("Eventually after the blood bath, the attacker scans the room one last time before leaving you still standing there in puddles of blood.")
        print("")
        print("Eventually you are found by rescue survices and sent to the hospital.")
        print("You will never know why you were spared instead of your many classmates, just that you were.")
        print("")
        print("Is this really a satisfactory ending for you?")
        print("Try your luck on another go.")

        if character == "Fish":  
            userAnswerfive = input()
            while True:
                if userAnswerfive == "1" or userAnswerfive.lower() == "give":
                    print("")
                    print("You shakily hand over your test to the attacker when you thought the teacher was looking away.")
                    print("The attacker grins at you and say that they are now best friends, and he will always protect you.")
                    print("You decide to try and change them for good now that you are friends.")
                    print("")
                    print("Three months later you take your new best friend out to dinner, without them killing anyone.")
                    print("This is progress.")
                    print("")
                    print("This is one happy ending, but how many can you find?")
                    print("Try again to find out.")
                    print("")
                    break
                elif userAnswerfive == "2" or userAnswerfive.lower() == "refuse":
                    print("")
                    print("You glare at them and say that you will not cheat for them.")
                    print("You watch as their face slowly crumples into anger and feel a sinking feeling in your gut.")
                    print("You hastaly apoligize but it is not enough.")
                    print("They stab you in the back with the knife and as you lie on the ground you see the attacker and your would-be friend staring back at you.")
                    print("As your vision starts to fade you see the tears running down the attackers face and the sadness in their eyes.")
                    print("The last thing you see in the attacker slowly turn around, head bowed and walk away.")
                    print("")
                    print("You died.")
                    print("")
                    print("Not only have they died you have broken their heart. I wonder if they will ever be able to trust again.")
                    print("")
                    print("Try again and find a better ending for everyone.")
                    print("")
                    break
                else:
                    print("")
                    print("That was not one of the opptions. ")
                    print("Your options are...")
                    print("")
                    print("1. Give.")
                    print("2. Refuse.")
                    print("")
                    userAnswerfive = input()






    

elif userAnswer == "2" or userAnswer.lower() == "skip":
    print("")
    print("You decide to keep walking down the hallway, straight past your math classroom.")
    print("You feel a little guilty as you walk to a quieter part of the school, heading towards the back exit")
    print("Suddenly, you hear footsteps running down the hall. Like, a lot of them. Coming your way towards the exit")
    print("You back up to get away from the people running in your direction, going into an empty classroom.")
    print("see your classmates running past the window of the empty classroom.")
    print("Realizing that these are your classmates, you realize something must have happened and so you open the door ad")
    skipUserAnswer = input()
    