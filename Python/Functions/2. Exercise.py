# Functions can also return values. This means that they can produce an output that can be used later in the code.
# This is useful when we want to perform calculations or manipulate data and then use the result in other parts of our program.
# Here is an example of a function that adds two numbers and returns the result:
def add_numbers(a, b):
    print("Adding numbers...")
    # This function returns the value of a + b.
    return a + b

shirtPrice = 20.00
tankTopPrice = 15.00
pantsPrice = 25.00
skirtPrice = 25.00

print("Welcome to the clothing store!")
print(f"A shirt costs {shirtPrice}.")
print(f"A tank top costs {tankTopPrice}.")
print(f"Pants cost {pantsPrice}.")
print(f"A skirt costs {skirtPrice}.")

print("")
print("Would you like pants or a skirt today?")
print("a. Pants")
print("b. Skirt")
pantsOrSkirt = input()

# Find price of the top they chose
bottomsCost = 0
if pantsOrSkirt == "a":
    bottomsCost = pantsPrice
elif pantsOrSkirt == "b":
    bottomsCost = skirtPrice

print("")
print("Would you like a shirt or a tank top today?")
print("a. Shirt")
print("b. Tank Top")
ShirtOrTank = input()

# Find price of the bottoms they chose
topsCost = 0
if ShirtOrTank == "a":
    topsCost = shirtPrice
elif ShirtOrTank == "b":
    topsCost = tankTopPrice

print("Thanks! Your total is:")
# TODO: Task 1, run the file as is. What is the output?
# TODO: Task 2, uncomment the following 2 lines. What is the output now?
# The demonstration here is that functions do not execute until they are explicitly called in the code.
total = add_numbers(bottomsCost, topsCost)
total = add_numbers(bottomsCost, topsCost)
print(total)