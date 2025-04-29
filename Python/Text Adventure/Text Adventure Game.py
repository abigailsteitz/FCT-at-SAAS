playAgain = "yes"
while playAgain == "yes":
    import random; print(random.randint(1, 100))
    print("If your number is 50+ you have a higher chance of being safe on your way home")
    print("Welcome to The Way Home!")
    print("It's a Friday afternoon and you are on your way home from school.")
    print("Do you choose to take the lightrail? yes or no?")
    choice = input().strip().lower()

    if choice == "yes":
        print("You start walking to the lightrail station.")
        print("you get mugged by a stranger on the way there.")
    elif choice == "no":
        print("You decide to wait for your Dad to pick you up.")
        print("Your friends are nearby and they invite you to go to the park with them.")
        print("Do you want to go with them? yes or no?")
        action = input().strip().lower()
        if action == "no":
            print("You dont want to go with them so you stay at school.")
            print("A the school collapses and you die")
        if action == "yes":
            print("You have a great time at the park with your friends.")
            print("After a few hours, you realize its time to head back to get picked up.")
            print("Do you head back to the car? yes or no?")
            carchoice = input().strip().lower()
            if carchoice == "no":
                print("Your Dad leaves you at the park and you have to walk home.")
                print("You get hit by a car and die.")
            if carchoice == "yes":
                print("You head back to the car and get picked up. Your driving home this time.")
                print("You see the light up ahead turn yellow.")
                print("Do you want to speed up and go through the light? yes or no?")
                speed = input().strip().lower()
                if speed == "yes":
                    print("You speed up and go through the light.")
                    print("You finally make it home, do you a) pull in or b) back in to the driveway?")
                    park = input().strip().lower()
                    if park == "a":
                        print("You switch gears too fast and shred your transmission.")
                        print("You have to pay for a new car.")
                    elif park == "b":
                        print("You make it home safely.")
                        print("Congratulations! You made it!")
                    else:
                        print("Invalid action. The game ends here.")
                elif speed == "no":
                    print("You get crushed by a falling tree.")
                else:
                    print("Invalid action. The game ends here.")
            elif action == "no":
                print("Your Dad forgets to pick you up and you have to walk home.")
            else:
                print("Invalid action. The game ends here.")
    else:
        print("Invalid choice. The game ends here.")
    print("Thanks for playing the Text Adventure Game!")
    playAgain = input("Would you like to play again? yes or no?").strip().lower()
    if playAgain == "yes":
        print("Great! Let's play again.")
        print("Restarting the game...")
    
    if playAgain == "no":
        print("Thanks for playing! Goodbye!")
        exit()