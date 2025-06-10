import random

print("you walk on to the track, an old asian man with a cane comes walking torwords you. The names master seiji he says ive coached more nascar winners than anyone before me i seee talent in you kid")


print("do you practice racing with master seiji?")

print("Would you like a) to practice with master seiji or b) not practice to practice with master seiji?")
variable = input()

if variable == "b":
  print("Oops you get a heart attack, start over")
  quit()

if variable == "a":
  print("Congrats you get new skills")

print("Gooey Tip: your a natural kid whats your name. The names Trickle... Fish Trickle")

print("dramatic backround music plays")

print("do you train with gooey tip or not")

print("would you like. a) to practice with gooey tip or b) not practice with gooey tip")
variable = input()

if variable == "a":
    print("congrats you are now ready for your first race!")

if variable == "b":
    print("you are banished to working a 9 to 5 for the rest of your life")
    quit()

print("fish trickle: thanks for the tips gooey your the man. Gooey: no problem... just watch out for that Gudeta guy hes been plotting on you for the race, hes one dirty racer")

print("would you like. a) to go to the race or b) keep practicing with Gooey Tip")
variable = input()
if variable == "a":
    print("good decesion be confident in your skills gooey tip taught you well")

if variable == "b":
    print("while you were practing Gudeta assassinated you, nice try")
    quit()

print("Gooey tip: alright rookie your first real race just relax and remeber everything we talked about, you're the man")
print("Gooey tip: that guy over thier hes Jared Golf...hes top of the food chian. back in 2012 Jared Golf killed your father in a deadily car accident...(Gooey Tip looks deaply in your eyes) Win this race for him")
print("Gudeta schemeing in the backround")

print("(race startin) 3,2,1, Gooooooo")

print("half way through the race Gudetas minions stole the tires off your wheels, do you contuine to race a) or take a pit stop b)")
variable = input()
if variable == "a":
    print("your car explodes and your barley alive you see your Gudeta kissing your parrot as you take your last breath on the track")
    quit()

if variable == "b":
    print("good choice")

print("Master Seiji says with asian accent: Good racing my student me and Gooey Tip are pround of you, these will help your drive faster(hands rocket boosters)")

print("oh no Jared Golf is in the lead by a lap roll a die to see if your rocket boosters work correctly")
print("press enter to roll the die")
input()
boosters = random.randint(1,10)
print(f"You rolled a {boosters}. If you roll more than a 5, good stuuf.")
if boosters > 5 :
    print("you zoom ahead but fall one meter short of the finish line, Jared Golf is in the lead")
else:
    print("you lose the race and get beaten up by Gudeta and Jared Golf")

print("Jared Golf comes up to you and pats your shoulder, he says, Jared Golf: you really gave me a run for my money kid, and my deepest condolences for your father. Jared lifts your arm into the air followed by the cheers of the crowd.")    

print("WE LOVE YOU FISH TRICKLE! They all say") 

print("The end")