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
    
    if action == "yes":
        print("You have a great time at the park with your friends.")
        print("After a few hours, you realize its time to head back to get picked up.")
        print("Do you head back to the car? yes or no?")
        action = input().strip().lower()
    elif action == "yes":
        print("You head back to the car and get picked up. Your driving home this time.")
        print("You see the light up ahead turn yellow.")
        print("Do you want to speed up and go through the light? yes or no?")
        speed = input().strip().lower()
        
    elif action == "no":
        print("Your Dad forgets to pick you up and you have to walk home.")
    else:
        print("Invalid action. The game ends here.")
else:
    print("Invalid choice. The game ends here.")
print("Thanks for playing the Text Adventure Game!")