import turtle

jo = turtle.Turtle()

jo.speed(10)


jo.penup()
jo.goto(-25, 15)
jo.pendown()

jo.setheading(0)

for i in range(8):
    jo.forward(10)
    jo.right(45)


jo.penup()
jo.goto(25, 15)
jo.pendown()

jo.setheading(0)

for i in range(8):
    jo.forward(10)
    jo.right(45)



jo.penup()
jo.goto(-180, 240)
jo.pendown()

for i in range(55):
    jo.right(7)
    for i in range(4):
        jo.forward(100)
        jo.right(90)

jo.penup()
jo.goto(180, 240)
jo.pendown()

for i in range(55):
    jo.right(7)
    for i in range(4):
        jo.forward(100)
        jo.right(90)

jo.penup()
jo.goto(-200, -90)
jo.pendown()

jo.setheading(270)
jo.circle(200, 180)



jo.hideturtle()
turtle.done()
