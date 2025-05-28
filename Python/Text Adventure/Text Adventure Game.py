def text_adventure_game():
    print("Welcome to terror land!")
    print("You are about to embark on a thrilling adventure.")
    print("You find yourself all alone in this world, you have no idea how you got here.")
    print("You realize you have made it to terror land, the place you have been trying to save for years..")
    print("You look around and see different people standing at the paths before you.")
    print("Each awaiting you to choose them as your guide.")
    print("You have four options:")
    print("1. Take the path with Auggie, a blacksmith.")
    print("2. Take the path with Steve, a traveler.")
    print("3. Take the path with Burt, a spy.")
    print("4. The last choice is to go out on your own.")
    print("What will you do?")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("You embark with Auggie, the blacksmith.")
    elif choice == "2":
        print("You embark with Steve, the traveler.")
    elif choice == "3":
        print("You embark with Burt, the spy.")
    elif choice == "4":
        print("You choose to go out on your own.")
    else:
        print("Invalid choice. Please restart the game and choose a valid option.")


text_adventure_game()