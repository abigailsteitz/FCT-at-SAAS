import turtle

turtle = turtle.Turtle()
turtle.color("green")
turtle.speed(10)
turtle.shape("turtle")
turtle.width(4)

def draw_concentric_squares(x, y, size, num, color):
    """ Draws concentric squares starting from the center. """
    turtle.penup()
    turtle.goto(x - size // 2, y - size // 2)  # Move to starting position
    turtle.pendown()
    turtle.color(color)
    
    for i in range(num):
        for _ in range(4):
            turtle.forward(size)
            turtle.left(90)
        size -= size / num
        turtle.penup()
        turtle.forward(size / (2))
        turtle.right(90)
        turtle.forward(size / (2))
        turtle.left(90)
        turtle.pendown()

def draw_concentric_triangles(x, y, size, num, color):
    """ Draws concentric triangles. """
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
    """ Draws a stair-like pattern. """
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
