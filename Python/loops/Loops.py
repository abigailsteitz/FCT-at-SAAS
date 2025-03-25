import turtle

Curry = turtle.Turtle()

for i in range (5):
    Curry.right(72)
    Curry.forward(100)

Curry.penup()
Curry.goto(-300, 100)
Curry.pendown()

for i in range (6):
    Curry.right(60)
    Curry.forward(100)

Curry.penup()
Curry.goto(-200, -100)
Curry.pendown()

for i in range (8):
    Curry.right(45)
    Curry.forward(100)

turtle.done()