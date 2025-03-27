import turtle 
jo = turtle.Turtle()
jo.speed(10)
jo.color("blue")


jo.penup()
jo.goto(0, 300)
jo.pendown()

jo.setheading(180)
for i in range(12):
    jo.forward(10*i)
    jo.right(120)

jo.setheading(300)

jo.penup()
jo.goto(0, 170)
jo.pendown()

for hexagon in range(12):
    jo.penup()
    jo.goto(jo.xcor() + 5, jo.ycor() + 8)
    jo.pendown()
    for i in range(6):
        jo.forward(10*hexagon)
        jo.right(60)

jo.penup()
jo.goto(10, 15)
jo.pendown()
jo.setheading(0)

for square in range(15):
    jo.penup()
    jo.goto(jo.xcor() - 4, jo.ycor()+4)
    jo.pendown()
    for i in range(4):
        jo.forward(8*square)
        jo.right(90)



jo.penup()
jo.goto(-300, -175)
jo.pendown()

jo.setheading(0)

for i in range(10):
    jo.forward(25)
    jo.left(90)
    jo.forward(25)
    jo.right(90)

jo.forward(87)

for i in range(10):
    jo.forward(25)
    jo.right(90)
    jo.forward(25)
    jo.left(90)
jo.forward(25)
jo.right(90)
jo.forward(25)
jo.right(90)
jo.forward(612)
jo.right(90)
jo.forward(25)


jo.hideturtle()

turtle.done()