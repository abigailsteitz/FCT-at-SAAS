import turtle

jo = turtle.Turtle()

jo.forward(100)

# Draw a square
for i in range(4):
    jo.forward(100)
    jo.right(90)

jo.penup()
jo.goto(-50,70)
jo.pendown()

# Draw a triangle
for i in range(36):
    jo.forward(70)
    jo.right(100)

jo.penup()
jo.goto(100,0)
jo.pendown()

# Draw a triangle
for i in range(6):
    jo.forward(100)
    jo.left(120)

jo.penup()
jo.goto(0,100)
jo.pendown()

# Draw a pentagon
for i in range(6):
    jo.forward(100)
    jo.left(72)

turtle.done()