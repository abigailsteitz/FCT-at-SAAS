import turtle

Lebron = turtle.Turtle()

for i in range(6):
    Lebron.forward(100)
    Lebron.right(60)

Lebron.penup()
Lebron.goto(69,69)
Lebron.pendown()

for i in range(8):
    Lebron.forward(100)
    Lebron.right(45)

Lebron.penup()
Lebron.goto(-69,-69)
Lebron.pendown()

radius = 100
Lebron.circle(radius)

turtle.done()