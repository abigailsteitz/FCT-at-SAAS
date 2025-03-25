import turtle
katelyn = turtle.Turtle()
katelyn.speed(10)
for i in range(8):
    katelyn.forward(100)
    katelyn.left(60)

for i in range(7):
    katelyn.forward(100)
    katelyn.right(60)

for i in range(10):
    katelyn.forward(100)
    katelyn.left(60)

for i in range(8):
    katelyn.forward(100)
    katelyn.right(60)

for i in range(5):
    katelyn.forward(100)
    katelyn.left(60)
for i in range(5):
    katelyn.forward(100)
    katelyn.right(60)

for i in range(6):
    katelyn.forward(100)
    katelyn.left(60)

for i in range(5):
    katelyn.forward(100)
    katelyn.left(60)

for i in range(6):
    katelyn.forward(100)
    katelyn.right(60)

    for i in range(3):
        katelyn.forward(100)
        katelyn.left(120)

katelyn.penup()
katelyn.goto(-100, -150)
katelyn.pendown()
#draw a circle
katelyn.circle(100, 360)
katelyn.left(90)
katelyn.forward(200)
turtle.done()