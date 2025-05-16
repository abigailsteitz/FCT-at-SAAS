import time
import pygame
import sys
path = "Python/Text Adventure/"


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

def initialize_game():
    # Initialize pygame and ask it to play the start sound
    pygame.init()
    pygame.mixer.init()

def play_sound(sound_file):
    sound = pygame.mixer.Sound(path + sound_file)
    sound.play()
    time.sleep(10)
    sound.stop()

def start_game():
    play_sound("wind noise.mp3")
    type_text("Welcome to the Ancient City Adventure!")
    time.sleep(1)
    name = input("What is your name, traveler? ")
    type_text(f"\nHello {name}, you find yourself in the ruins of an ancient city...")

    choice1 = input("\nYou find a mysterious goblet. Do you:\n1. Pick it up\n2. Leave it\n> ")
    if choice1 == "1":
        type_text("You pick up the goblet. Suddenly, a map falls out of it.")
        gobletsound = "mystery.mp3"
        play_sound(gobletsound)
    else:
        type_text("You leave the goblet, but a gust of wind knocks it over and a map falls out anyway.")
        gobletsound = "mystery.mp3"
        play_sound(gobletsound)

    choice2 = input("\nDo you:\n1. Follow the map\n2. Explore the city on your own\n> ")
    if choice2 == "1":
        type_text("You follow the map. It leads to an eerie lighthouse on the edge of the cliffs.")
    else:
        type_text("You wander the city but end up at a lighthouse anyway. Fate, perhaps?")

    whisperingSound = "whispering.mp3"
    play_sound(whisperingSound)
    choice3 = input("\nYou hear faint whispering from the top of the lighthouse. Do you:\n1. Enter\n2. Stay outside\n> ")
    if choice3 == "1":
        type_text("You climb to the top and find someone else who followed the map.")
    if choice3 == "2":
        type_text("A person comes out of the lighthouse. They look friendly.")
        choice4 = input("\nDo you:\n1. Recruit them to your quest\n2. Continue solo\n> ")
        if choice4 == "1":
            companion = True
            type_text("They agree to join you.")
        else:
            companion = False
            type_text("You decide to stay solo.")
    else:
        type_text("You stay outside, but the person from the lighthouse comes out and joins you anyway.")
        companion = True
    
    ZeusSound = "thunder.mp3"
    play_sound(ZeusSound)
    type_text("\nSuddenly, the sky cracks open. Zeus descends, furious.")
    type_text('How dare you steal my goblet!" he roars.')

    choice5 = input("\nDo you:\n1. Apologize\n2. Stand your ground\n> ")
    if choice5 == "1":
        type_text("Zeus forgives you... a little. He demands the goblet back.")
        end = "neutral"
    else:
       type_text("Zeus prepares to strike you down with lightning!")
    if companion:
            type_text("Your companion steps forward. 'I know what to do with the goblet!'")
            choice6 = input("\nDo you:\n1. Hand it to them\n2. Keep it for yourself\n> ")
            if choice6 == "1":
                type_text("\nYour companion channels its power and defeats Zeus with a blinding flash of light!")
                ending = "win"
            else:
                type_text("\nYou try to keep the goblet, but Zeus blasts you with lightning. You lose.")
                ending = "lose"
    else:
            type_text("\nYou have no help. Zeus defeats you easily.")
            ending = "lose"

    if ending == "win":
        type_text("\nCongratulations! You've won the battle and saved the ancient city!")
        victorySound = "inception.mp3"
        play_sound(victorySound)

    elif ending == "lose":
        type_text("\nYou have been defeated. The goblet returns to the sky, and the city is lost once more.")
        losesound = "Gameover.mp3"
        play_sound(losesound)
    else:
        type_text("\nYou avoided total destruction... but the adventure continues another day.")

initialize_game()
start_game()

