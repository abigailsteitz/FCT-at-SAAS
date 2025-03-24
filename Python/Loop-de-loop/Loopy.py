import turtle

# Set up the turtle
artist = turtle.Turtle()
artist.speed(3)

# Draw a triangle
artist.penup()
artist.goto(-200, 100)  # Move to starting position
artist.pendown()
artist.color("blue")
for _ in range(3):  # Loop for 3 sides
    artist.forward(100)
    artist.left(120)

# Draw a square
artist.penup()
artist.goto(0, 100)  # Move to starting position
artist.pendown()
artist.color("green")
for _ in range(4):  # Loop for 4 sides
    artist.forward(100)
    artist.left(90)

# Draw a star
artist.penup()
artist.goto(200, 100)  # Move to starting position
artist.pendown()
artist.color("red")
for _ in range(5):  # Loop for 5 points
    artist.forward(100)
    artist.right(144)

# Finish the drawing
turtle.done()