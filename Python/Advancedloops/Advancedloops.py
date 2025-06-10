import turtle

tina = turtle.Turtle()
tina.color("purple")
tina.speed(10)
tina.shape("turtle")
tina.width(10)

# make a stair case
for i in range(10):
    tina.forward(5)
    tina.right(30)
    tina.forward(5)
    tina.left(30)

tina.penup()
tina.goto(0, 0)
tina.pendown()

# Draw a square spiral
for i in range(20):
    tina.forward(10*i)
    tina.right(60)  

tina.penup()
tina.goto(0, 0)
tina.pendown()

# Draw a hexagonal concentric spiral
for banana in range(30):
    for i in range(6):
        tina.forward(30*banana)
        tina.left(30)

    tina.penup()
    tina.goto(tina.xcor() +5,tina.ycor())
    tina.pendown()

# Draw a triangle sprial
turtle.done()