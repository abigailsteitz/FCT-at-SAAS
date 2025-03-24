import turtle

# Set up the turtle
star = turtle.Turtle()
star.speed(2)

# Draw a 5-point star
for _ in range(5):
    star.forward(100)
    star.right(144)

# Hide the turtle and display the window
star.hideturtle()
turtle.done()