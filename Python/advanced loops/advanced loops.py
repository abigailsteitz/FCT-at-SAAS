import turtle
tom = turtle.Turtle()

tom.color("green")
tom.speed(10)
tom.shape("turtle")
tom.width(4)

tom.penup()
tom.goto(-200,-200)
tom.pendown()


#stair up right
for i in range (6):
    tom.left(90)
    tom.forward(25)
    tom.right(90)
    tom.forward(25)

#platform
tom.forward(150)

#stair down right
for i in range (6):
    tom.forward(25)
    tom.right(90)
    tom.forward(25)
    tom.left(90)


tom.penup()
tom.goto(25,35)
tom.pendown()
tom.color("red")

#square
for banana in range (17):
    for i in range(4):
        tom.forward(10*banana)
        tom.left(90)

    tom.penup()
    tom.goto(tom.xcor() -5, tom.ycor() -5)
    tom.pendown()


tom.penup()
tom.goto(22,150)
tom.pendown()
tom.color("blue")

#triangle
for i in range(13):
    tom.left(120)
    tom.forward(10*i)


turtle.done()