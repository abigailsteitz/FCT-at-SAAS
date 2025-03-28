import turtle

def draw_spiral_square(x, y, size, num, color):
    """Draws a nested square spiral."""
    turtle.penup()
    turtle.goto(x - size // 2, y - size // 2)  # Move to the starting position
    turtle.pendown()
    turtle.color(color)

    for i in range(num):
        for _ in range(4):
            turtle.forward(size)
            turtle.right(90)
        size -= size / num
        turtle.penup()
        turtle.forward(size / (2))
        turtle.right(90)
        turtle.forward(size / (2))
        turtle.left(90)
        turtle.pendown()

def draw_spiral_triangle(x, y, size, num, color):
    """Draws a nested triangle spiral."""
    turtle.penup()
    turtle.goto(x - size // 2, y)  # Move to starting position
    turtle.pendown()
    turtle.color(color)

    for i in range(num):
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
        size -= size / num
        turtle.penup()
        turtle.forward(size / 2)
        turtle.right(120)
        turtle.forward(size / 2)
        turtle.left(120)
        turtle.pendown()

def draw_steps(x, y, step_size, steps, color):
    """Draws a stair-like pattern at the base."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)

    for _ in range(steps):
        turtle.forward(step_size)
        turtle.left(90)
        turtle.forward(step_size)
        turtle.right(90)

    turtle.forward(step_size)

    for _ in range(steps):
        turtle.right(90)
        turtle.forward(step_size)
        turtle.left(90)
        turtle.forward(step_size)

# Initialize turtle
turtle.speed(0)
turtle.bgcolor("white")  # Background color

# Draw the step-like base
draw_steps(-100, -100, 20, 5, "green")

# Draw the spiral square (house base)
draw_spiral_square(0, 0, 200, 10, "red")

# Draw the spiral triangle (roof)
draw_spiral_triangle(0, 100, 200, 10, "blue")

# Finish
turtle.hideturtle()
turtle.done()