import turtle

ka = turtle.Turtle()

for i in range(4):
    ka.forward(100)
    ka.left(90)

ka.penup()
ka.goto(200, 300)
ka.pendown()

# Draw a triangle
for i in range(3):
    ka.forward(100)
    ka.left(120)

# Draw a circle
ka.penup()
ka.goto(-200, 200)
ka.pendown()
ka.circle(100)

ka.penup()
ka.goto(-200, -200)
ka.pendown()
for i in range(6):
    ka.left(60)
    ka.forward(100)

ka.penup()
ka.goto(200, -200)
ka.pendown()
for i in range(9):
    ka.left(160)
    ka.forward(300)

# Draw a star
ka.penup()
ka.goto(0, 0)
ka.pendown()
for i in range(5):
    ka.forward(100)
    ka.right(144)

# Draw a spiral
ka.penup()
ka.goto(320, -200)
ka.pendown()
for i in range(36):
    ka.forward(i * 10)
    ka.right(144)

# Draw a circle spiral
ka.penup()
ka.goto(-320, 200)
ka.pendown()
for i in range(20):
    ka.circle(i * 10)
    ka.right(144)

turtle.done()

