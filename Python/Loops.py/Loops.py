import turtle

Lucy = turtle.Turtle()

for i in range(6):
    Lucy.forward(100)
    Lucy.right(60)

Lucy.penup()
Lucy.goto(69,69)
Lucy.pendown()

for i in range(8):
    Lucy.forward(100)
    Lucy.right(45)

Lucy.penup()
Lucy.goto(-69,-69)
Lucy.pendown()

radius = 100
Lucy.circle(radius)

turtle.done()