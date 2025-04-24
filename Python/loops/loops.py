import turtle

bonquifa = turtle.Turtle()
bonquifa.speed(10)

bonquifa.penup()
bonquifa.goto(200, 200)
bonquifa.pendown()

for i in range(4):
    bonquifa.forward(100)
    bonquifa.left(90)

bonquifa.penup()
bonquifa.goto(200, 22)
bonquifa.pendown()

#make a triangle
for i in range(3):
    bonquifa.forward(100)
    bonquifa.left(120)

bonquifa.penup()
bonquifa.goto(180, -100)
bonquifa.pendown()

for i in range(5):
    bonquifa.forward(150)
    bonquifa.right(144)

bonquifa.penup()
bonquifa.goto(0, 200)
bonquifa.pendown()

for i in range(30):
    bonquifa.forward(i * 5)
    bonquifa.left(45)

bonquifa.penup()
bonquifa.goto(-100, -100)
bonquifa.pendown()

for i in range(9):
    bonquifa.forward(70)
    bonquifa.left(360 / 9)

turtle.done()