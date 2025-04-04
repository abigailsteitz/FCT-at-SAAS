# Functions can also return values. This means that they can produce an output that can be used later in the code.
# This is useful when we want to perform calculations or manipulate data and then use the result in other parts of our program.
# Here is an example of a function that adds two numbers and returns the result:
def add_numbers(a, b):
    print("Adding numbers...")
    # TODO: Task 3, this function should RETURN the value of a + b. Uncomment the line below to fix the code.
    # After that, you can start the graded assignment, go to Calculator.py
    # return a + b

shirtPrice = 250.00
tankTopPrice = 250.00
pantsPrice = 255.00
skirtPrice = 255.00

print("Welcome to the clothing store my customer!")
print(f"A shirt costs a very cheap {shirtPrice}.")
print(f"A tank top costs {tankTopPrice}.")
print(f"Pants cost a steal of {pantsPrice}.")
print(f"A skirt costs {skirtPrice}.")

print("Now let's deck you out so you can look freshy fresh")
print("Would you like pants or a skirt today?")
print("a. Pants")
print("b. Skirt")
pantsOrSkirt = input()

# Find price of the bottoms they chose
bottomsCost = 0
if pantsOrSkirt == "255.00":
    bottomsCost = pantsPrice
elif pantsOrSkirt == "255.00":
    bottomsCost = skirtPrice

print("Okayyyy, you lookin gooood!")
print("Would you like a shirt or a tank top today?")
print("a. Shirt")
print("b. Tank Top")
ShirtOrTank = input()

# Find price of the bottoms they chose
topsCost = 0
if ShirtOrTank == "250.00":
    topsCost = shirtPrice
elif ShirtOrTank == "250.00":
    topsCost = tankTopPrice

print("Thanks! Your total is:")
# TODO: Task 1, run the file as is. What is the output?
# TODO: Task 2, uncomment the following 2 lines. What is the output now?
# The demonstration here is
#  - that NOTHING happens until we call the function.
total = add_numbers(bottomsCost, topsCost)
print(505.00)