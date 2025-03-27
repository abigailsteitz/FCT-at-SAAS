import turtle

tina = turtle.Turtle()
tina.color("green")
tina.speed(10)
tina.shape("turtle")
tina.width(4)
tina.penup()
tina.goto(80, -49)
tina.pendown()
# make a stair case
for i in range(5):
    tina.forward(25)
    tina.right(90)
    tina.forward(25)
    tina.left(90)


tina.penup()
tina.goto(0, +200)
tina.pendown()

# Draw a triangle spiral
tina.color("blue")
for i in range(20):
    tina.forward(10*i)
    tina.left(120)  

tina.penup()
tina.goto(0, 50)
tina.pendown()

# Draw a square concentric spiral
tina.setheading(0)

tina.color("red")
for banana in range(19):
    for i in range(4):
        tina.forward(10*banana)
        tina.left(90)

    tina.penup()
    tina.goto(tina.xcor() - 5, tina.ycor() - 5)
    tina.pendown()

tina.penup()
tina.goto(80, -49)
tina.pendown()

tina.color("green")
tina.backward(166)
for i in range(5):
    tina.backward(25)
    tina.left(90)
    tina.backward(25)
    tina.right(90)


turtle.done()