# Welcome to the Python Functions Exercise!
# In this exercise, I will explain what a function is and how to create one in Python.

# Said Technically: A function is a reusable piece of code that performs a specific task.
# It can take inputs (called parameters) and return an output.
# Functions help us organize our code and avoid repetition.

# Said with an Analogy: A function is like a cookie cutter. It CUTS cookies. We can use it to cut many cookies. It is re-usable.

# This is a function DEFINITION. It uses the 'def' keyword.
# It has a PARAMETER called 'name'.
# The function prints a greeting message using the provided name.
def greet(name):
    print(f"Hello, {name}! Thanks for coming to my birthday party!")

# This is a function CALL. It uses the function DEFINITION above.
# To follow the analogy, we are using the cookie cutter to cut a cookie.
# When we CALL the function, we are cutting a cookie.
# TODO: Task 1, replace 'name' with your name, and run the code.
greet("nick")

# TODO: Task 2, this variable 'names' is empty, give it a list of your friends' names.
names = [ 'indy',  'miles',  'nick',]

# TODO: Task 3, use a for loop to iterate over the list of names and call the greet function for each name.
for name in names:
    greet(name)
# After Task 3, go to the next exercise file to learn about return values.