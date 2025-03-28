import turtle

def draw_square(x, y, size, depth, color):
    """Draws nested squares."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    
    for i in range(depth):
        for _ in range(4):
            turtle.forward(size - (i * 10))
            turtle.right(90)
        turtle.penup()
        turtle.goto(x + (i + 1) * 5, y - (i + 1) * 5)
        turtle.pendown()

def draw_triangle_spiral(x, y, size, depth, color):
    """Draws a triangular spiral."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    
    for i in range(depth):
        for _ in range(3):
            turtle.forward(size + (i * 10))  # Increase size with each iteration
            turtle.left(120)  # Turn to form a triangle
        size += 10  # Increment the size for the spiral effect

def draw_steps(x, y, step_size, steps, color):
    """Draws the stepped base."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    
    for _ in range(steps):
        turtle.forward(step_size)
        turtle.right(90)
        turtle.forward(step_size)
        turtle.left(90)

    turtle.forward(step_size)  # Final step to complete the shape

# Setup Turtle
turtle.speed(0)
turtle.bgcolor("white")

# Draw the elements
draw_square(-50, -50, 100, 10, "red")     # House Body
draw_triangle_spiral(-50, 50, 50, 10, "blue")   # Roof
draw_steps(-100, -100, 10, 10, "green")   # Steps on the base

# Finish
turtle.hideturtle()
turtle.done()
