import random
def saloontab (a, b):
    print("Adding numbers...")
    return a + b
print("Welcome to the wild west")
print("You are traveling through the town of telford, texas.")
    
print("What would you like to do?")
print("1. Enter dual with stranger")
print("2. Talk to stranger")
print("3. Enter saloon")
print("4. Quit")
choice = input("Enter the number of your choice: ")

if choice == "1":
    print("Your dual has started. Shoot by picking 6 or 7.")
    choice = input("Enter your choice: ")
    if choice == "6":
        print("You were to slow and got shot!")
    elif choice == "7":
        print("You won the dual with a head shot.")
    else:
        print("Invalid choice. Please try again.")

print("Pick next option")
print("1. Enter dual with stranger")
print("2. Talk to stranger")
print("3. Enter saloon")
print("4. Quit")
    



        
if choice == "2":
    print("Hi stranger, I'm lacy how can I help you?")
    print("1. I need a drink")
    print("Follow me to the Saloon")
    print("Choose 8 to follow Lacy and 9 to leave")
    choice = input("Enter your choice: ")
    if choice == "8":
        print("You enter the saloon and drink a beer")
    elif choice == "9":
        print("You walked away")
    else:
        print("Invalid choice. Please try again.")


BeerCost = 0.50
WhiskeyCost = 1.00
VodkaCost = 2.00



if choice == "3":
    print("You have entered the saloon, look at the menu for drinks")
    print("10. Beer")
    print("11. Whiskey")
    print("12. Vodka")
    print("select which drink you want")
    
    drinkCost = 0
    choice = input("Enter your choice: ")

    #TODO: assign drinkCost based on the drink selected
    if choice == "10":
        print("You ordered a beer")
        drinkCost = BeerCost
    elif choice == "11":
        print("You ordered a whiskey")
        drinkCost = WhiskeyCost
    elif choice == "12":
        print("You ordered a vodka")
        drinkCost = VodkaCost
    else:
        print("Invalid choice. Please try again.")

    #TODO: ask the user for some food choice
    # IF statement stuff


    burgerCost = 5.00 
    hotdogCost = 3.00
    saladCost = 4.00

    print("look at the menu for food")
    print("13. burger")
    print("14. hotdog")
    print("15. salad")
    print("select which food you want")



    foodCost = 0
    choice = input("Enter your choice: ")

    if choice == "13":
        print("You ordered a burger")
        foodCost = 5.00
    elif choice == "14":
        print("You ordered a hotdog")
        foodCost = 3.00
    elif choice == "15":
        print("You ordered a salad")
        foodCost = 4.00
    else:
        print("Invalid choice. Please try again.")
   

    #TODO: use the drinkCost and foodCost to calculate the total cost of the meal, call your function to do this

    total = saloontab(drinkCost, foodCost)
    print("Thanks! Your total is:")
    print(total)

