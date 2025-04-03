import turtle

# Set up the turtle
artist = turtle.Turtle()
artist.speed(3)

# Draw a pentagon
artist.penup()
artist.goto(-200, 100)  # Move to starting position
artist.pendown()
artist.color("blue")
for _ in range(5):  # Loop for 5 sides
    artist.forward(100)
    artist.left(72)

# Draw an octagon
artist.penup()
artist.goto(0, 100)  # Move to starting position
artist.pendown()
artist.color("green")
for _ in range(8):  # Loop for 8 sides
    artist.forward(100)
    artist.left(45)

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