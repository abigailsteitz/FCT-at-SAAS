import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Blue Triangle Spiral")

# Set up the turtle
spiral = turtle.Turtle()
spiral.speed(0)
spiral.color("blue")

# Draw the triangle spiral
size = 5
for _ in range(100):
    spiral.forward(size)
    spiral.left(120)  # Triangle angle
    size += 2  # Increment size for the spiral effect



square = turtle.Turtle()
square.speed(0)
square.color("red")
square.penup()
square.goto(-10,-170)
square.pendown()

square_size = 20

for _ in range(10):  # Number of squares
    for _ in range(4):  # Draw a square
        square.forward(square_size)
        square.left(90)
    square.penup()
    square.backward(10)  # Adjust position for the next square
    square.right(90)
    square.forward(10)
    square.left(90)
    square.pendown()
    square_size += 20  # Increment size for the next square

square.hideturtle()

# Draw a green staircase
staircase = turtle.Turtle()
staircase.speed(0)
staircase.color("green")
staircase.penup()
staircase.goto(-200,-362)
staircase.pendown()

step_size = 20
num_steps = 5

for _ in range(num_steps):
    staircase.forward(step_size)
    staircase.left(90)
    staircase.forward(step_size)
    staircase.right(90)

staircase.forward(200)

for i in range (num_steps):
    staircase.right(90)
    staircase.forward(step_size)
    staircase.left(90)
    staircase.forward(step_size)

staircase.hideturtle()


# Hide the turtle and finish
spiral.hideturtle()
screen.mainloop()

