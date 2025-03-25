import turtle
tom = turtle.Turtle()


for i in range (4):
    tom.forward(50)
    tom.right(90)

tom.penup()
tom.goto(60,-60)
tom.pendown()

for i in range (3):
    tom.forward(100)
    tom.left(120)

tom.penup()
tom.goto(-100,100)
tom.pendown()

for i in range (8):
    tom.forward(70)
    tom.left(45)

tom.penup()
tom.goto(50, 50)
tom.pendown()

for i in range (5):
    tom.forward(50)
    tom.right(36)
    tom.forward(50)
    tom.left(108)

tom.penup()
tom.goto(-60, -60)
tom.pendown()

for i in range (5):
    tom.forward(100)
    tom.right(72)

turtle.done()

