import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)

def draw_star(x, y, size=40):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.penup()

def draw_turtle_shape():
    t.penup()
    t.goto(0, -30)
    t.pendown()
    t.setheading(0)
    t.color("green")
    t.begin_fill()
    t.circle(30)  # body
    t.end_fill()

    # Head
    t.penup()
    t.goto(0, 10)
    t.pendown()
    t.setheading(90)
    t.begin_fill()
    t.circle(12, 180)
    t.end_fill()

    # Legs
    for angle, pos in [(45, (20, -10)), (135, (-20, -10)), (225, (-20, -50)), (315, (20, -50))]:
        t.penup()
        t.goto(pos)
        t.pendown()
        t.setheading(angle)
        t.begin_fill()
        t.circle(8, 180)
        t.end_fill()

    # Tail
    t.penup()
    t.goto(0, -60)
    t.p