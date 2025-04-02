import turtle

# Function to draw nested squares
def draw_squares(t, size, count, color):
    t.color(color)
    for _ in range(count):
        for _ in range(4):
            t.forward(size)
            t.left(90)
        size -= 10
        t.penup()
        t.goto(t.xcor() + 5, t.ycor() - 5)
        t.pendown()

# Function to draw nested triangles
def draw_triangles(t, size, count, color):
    t.color(color)
    for _ in range(count):
        for _ in range(3):
            t.forward(size)
            t.left(120)
        size -= 10
        t.penup()
        t.goto(t.xcor() + 5, t.ycor() - 5)
        t.pendown()

# Function to draw steps
def draw_steps(t, step_size, count, color):
    t.color(color)
    for _ in range(count):
        t.forward(step_size)
        t.left(90)
        t.forward(step_size)
        t.right(90)

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)

# Draw the red squares
t.penup()
t.goto(-50, -50)
t.pendown()
draw_squares(t, 100, 10, "red")

# Draw the blue triangles
t.penup()
t.goto(-50, 50)
t.pendown()
draw_triangles(t, 100, 10, "blue")

# Draw the green steps (left side)
t.penup()
t.goto(-100, -150)
t.setheading(0)
t.pendown()
draw_steps(t, 10, 10, "green")

# Draw the green steps (right side)
t.penup()
t.goto(0, -150)
t.setheading(0)
t.pendown()
draw_steps(t, 10, 10, "green")

# Finish
t.hideturtle()
screen.mainloop()