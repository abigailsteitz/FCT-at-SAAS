import turtle

# Setup
tina = turtle.Turtle()
tina.speed(0)  # Fastest drawing speed
tina.width(2)  # Pen width
tina.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set background color

# Function to draw a single petal
def draw_petal(size, angle, color):
    tina.color(color)
    tina.begin_fill()
    for _ in range(2):
        tina.circle(size, angle)  # Draw an arc
        tina.left(180 - angle)  # Turn to draw the other side of the petal
    tina.end_fill()

# Function to draw a spiral flower
def draw_spiral_flower(petal_count, initial_size, size_increment, angle_increment):
    colors = ["red", "orange", "yellow", "pink", "purple", "blue", "green"]  # Petal colors
    size = initial_size  # Start with the initial petal size
    angle = 0  # Start angle for the spiral

    for i in range(petal_count):
        color = colors[i % len(colors)]  # Cycle through colors
        draw_petal(size, 60, color)  # Draw a petal
        tina.penup()
        tina.setheading(angle)  # Rotate for the spiral
        tina.forward(size_increment)  # Move outward for the spiral
        tina.pendown()
        angle += angle_increment  # Increment the angle for the spiral
        size += size_increment / 5  # Gradually increase petal size

# Draw the spiral flower
draw_spiral_flower(petal_count=50, initial_size=30, size_increment=20, angle_increment=20)

# Finish
turtle.done()