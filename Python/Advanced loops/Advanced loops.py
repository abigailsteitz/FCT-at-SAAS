import turtle

tina = turtle.Turtle()
tina.color("green")
tina.speed(10)
tina.shape("turtle")
tina.width(4)

tina.penup()
tina.goto(100, -200)
tina.pendown()

# make a stair case
for i in range(10):
    tina.forward(25)
    tina.right(90)
    tina.forward(25)
    tina.left(90)

tina.penup()
tina.goto(100, -200)
tina.pendown()
tina.goto(-100,-200)


for i in range(10):
    tina.backward(25)
    tina.left(90)
    tina.backward(25)
    tina.right(90)


tina.penup()
tina.goto(0, 0)
tina.pendown()

tina.setheading(-300)

# Draw a square spiral
for i in range(20):
    tina.forward(10*i)
    tina.right(120)  

tina.penup()
tina.goto(0, -150)
tina.pendown()

tina.setheading(0)

# Draw a hexagonal concentric spiral
for banana in range(10):
    for i in range(4):
        tina.forward(10*banana)
        tina.left(90)

    tina.penup()
    tina.goto(tina.xcor() -5,tina.ycor() -5)
    tina.pendown()

turtle.done()