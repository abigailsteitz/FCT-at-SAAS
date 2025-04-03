import turtle

tina = turtle.Turtle()
tina.speed(10)

# Draw staircase
tina.color("green")
for i in range(10, 0, -1):
    tina.forward(20)
    tina.left(90)
    tina.forward(20)
    tina.right(90)

# Move to square position
tina.penup()
tina.goto(-100, 0)
tina.pendown()

# Draw square spiral
tina.color("red")
for i in range(10):
    for _ in range(4):
        tina.forward(20 * i)
        tina.right(90)

    tina.penup()
    tina.goto(tina.xcor()-9, tina.ycor()+9)
    tina.pendown()

# Move to triangle position
tina.penup()
tina.goto(-90, 200)
tina.pendown()

tina.penup()
tina.goto(tinaXcor()-9, tina.ycor()+9)
tina.pendown()

# Draw triangle spiral
tina.color("blue")
for i in range(10, 0, -1):
    for _ in range(3):
        tina.forward(20 * i)
        tina.right(120)

turtle.done()