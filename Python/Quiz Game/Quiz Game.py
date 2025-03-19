import time
import sys
C3PO = "\033[1;33m"

R2D2 = "\033[34m"
score = 0



def type_text(text, delay=0.033):
    for char in text:
        sys.stdout.write(char)  #  Write the character without moving to a new line
        sys.stdout.flush()       # Force the output to be displayed immediately
        time.sleep(delay)        # Wait for a short period before displaying the next character

def type_text(text, delay=0.033):
    # Split the text into lines by newline characters
    lines = text.split('\n')
    
    for line in lines:
        for char in line:
            sys.stdout.write(char)  # Write the character without moving to a new line
            sys.stdout.flush()       # Force the output to be displayed immediately
            time.sleep(delay)        # Wait for a short period before displaying the next character
        
        # After each line, print a newline to move to the next line
        sys.stdout.write('\n')  # Move to the next line after finishing the current line
        sys.stdout.flush()      # Ensure the newline is printed
 
time.sleep (0.1)
sys.stdout.write(C3PO) 
type_text("Hello Everyone! I am C-3PO, human-cyborg relations, and this is my counterpart, R2-D2")
sys.stdout.write("\n")
sys.stdout.flush()
time.sleep(0.4)
sys.stdout.write(R2D2)
type_text("Beep beep beep beep boop")
sys.stdout.write(C3PO + "\n")
sys.stdout.flush()
time.sleep(0.7)
type_text("Thank you, R2. I was just getting to that. R2 tells me you are here to take a Star Wars quiz. I will warn you, it won't be easy, R2 made the questions a little too hard-")
sys.stdout.write(R2D2 + "\n")
sys.stdout.flush()
time.sleep(0.8)
type_text("(beep of objection)")
sys.stdout.write(C3PO + "\n")
sys.stdout.flush()
time.sleep(0.8)
type_text("Don't bother denying it, R2! Anyway, let's begin")
time.sleep(2)
type_text("Q: When was the first Star Wars film released?")
type_text("a) 1980")
type_text("b) 1975")
type_text("c) 1977")
type_text("d) 1983")
userAnswer = input()
print (userAnswer)

if userAnswer == "c":
  type_text("Wonderful! Wonderful, I never doubted you for a second!")
  score = score + 1
elif userAnswer == "c":
  type_text("I'm very sorry, that's incorrect")
  
time.sleep(2)

type_text("Now, let's move on")
type_text("Q: In Episode One, The Phantom Menace, Queen Amidala's ship escaped the Trade Federation Blockade but only by a hair. Their ship was under attack, their shields were down, and they were going to be destroyed for sure. Who saved them?")
type_text("a) Qui-Gon Jinn")
type_text("b) R2D2")
type_text("c) Obi-Wan Kenobi")
type_text("d) Jar Jar Binks")
userAnswer = input()
print (userAnswer)
if userAnswer == "b":
  score = score + 1
  type_text("Aha! You are correct! It is, in fact R2-D- Wait, R2, did you write this question about yourself?")
  sys.stdout.write(R2D2 + "\n")
  time.sleep(0.7)
  type_text("(Beep of affirmation)")
  sys.stdout.write(C3PO + "\n")
  time.sleep(0.9)
  type_text("Well, I-")
  time.sleep(0.4)
  type_text("I suppose you've earned it R2. In any case, let us move on.")
elif userAnswer == "b":
  type_text("Oh dear. Wrong, I'm afraid")
time.sleep(1)
type_text("Oh, it looks like you've given me a question too!")
time.sleep(0.7)

type_text ("Q. How many forms of communication am I fluent in?")
type_text("a) 7 thousand")
type_text("b) 8 billion")
type_text("c) 7 million")
type_text("d) 6 million")
userAnswer = input()
print (userAnswer)

if userAnswer == "d":
  score = score + 1
  type_text("YES! You knew. And may I add, that if you ever require my services, I shall be available. For instance, I'm quite experienced with binary loadlifters-")
  sys.stdout.write(R2D2 + "\n")
  time.sleep(0.04)
  type_text("BLOOP (ANGRY BEEP)")
  sys.stdout.write(C3PO + "\n")
  time.sleep(0.5)
  type_text("Don't call me long-winded you malfunctioning garbage dispenser! Oh, excuse me, where are my manners.")
if userAnswer == "a":
  type_text("(In hurt voice) 7 thousand? Do you really think so little of me?")
if userAnswer == "b": 
  type_text("Well, I'm flattered you think I know that many, but no.")
if userAnswer == "c":
  type_text("No, it is not")

time.sleep(1)
type_text("Now, we are getting into the final questions.")
type_text("Q. In the Empire Strikes Back, Masters Han, Leia, Chewbacca, and even myself were aprehended by the Empire after our arrival. I was even SHOT! It was all quite scary. Who found out we were headed there and reported us to the Empire?")
type_text("a) Darth Vader")
type_text("b) Lando Calrissian")
type_text("c) Boba Fett")
type_text("d) Jabba the Hutt")
userAnswer = input()
print (userAnswer)
if userAnswer == "c":
  score = score + 1
  type_text("Congratulations! You know, to this day, I still don't think my joints have held up quite the same.")
if userAnswer == "b":
  type_text("Well, HE didn't, but I must say he certainly could have helped us earlier. 'had no choice' pffftt!")
  sys.stdout.write(R2D2 + "\n")
  time.sleep(0.4)
  type_text("beep beep boop-")
  sys.stdout.write(C3PO + "\n")
  time.sleep(0.4)
  type_text("Well, of course he was under pressure. Still though, he could have at least warned us...")
if userAnswer == "a" or userAnswer == "d":
  type_text("It was not them, though they were happy to join in on the 'fun.'")
time.sleep(1)

type_text("Q. And for our final question, which wonderful species helped us destroy the Death Star's shield generator?")
type_text("a) Ewoks")
type_text("b) Wookies")
type_text("c) Bothans")
type_text("d) Ugnauts")
userAnswer = input()
print (userAnswer)
if userAnswer == "a":
  score = score + 1
  type_text("Of course! I don't know what we would have done without them. We would have been destroyed for sure-")
  sys.stdout.write(R2D2 + "\n")
  time.sleep(0.4)
  type_text("BEEP BEEP! (Argumentative beeps")
  sys.stdout.write(C3PO + "\n")
  time.sleep(0.4)
  type_text("Yes, yes, but we were able to patch you up soon enough after that, so no problem in the long run, right R2?")
elif userAnswer == "a":
  type_text("Terribly sorry. I'm afriad-")
  time.sleep(0.6)
  type_text("You're doomed")
  
time.sleep (1)

if score == "5":
  type_text("Well, you DO know your trivia. In that case, I have a special question for you")
  type_text("Q. Who was the first character in A New Hope to say the famous phrase, 'I have a bad feeling about this?'")
  type_text("a) Luke Skywalker")
  type_text("b) Han Solo")
  type_text("c) Leia Organa")
  type_text ("d) Obi-Wan Kenobi")
  userAnswer = input()
  print (userAnswer)
  if userAnswer == "a":
    type_text("It WAS Master Luke! Although I hear some say it was Master Han")
  elif userAnswer == "a":
    type_text("No, it was Master Luke.")

type_text("Congratulations on your impressive score of " + str(score) + ", and I we hope you've enjoyed your quiz! R2 and I were proud to host!")
sys.stdout.write(R2D2 + "\n")
time.sleep(0.9)
type_text("Beep Boop Boop!")