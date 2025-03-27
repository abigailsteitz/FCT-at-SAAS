import turtle

tina = turtle.Turtle()
tina.color("green")
tina.speed(10)
tina.shape("turtle")
tina.width(4)


tina.forward(200)
tina.left(180)
tina.forward(400)
tina.left(180)
tina.forward(400)

# make a stair case
for i in range(5):
    tina.forward(25)
    tina.right(90)
    tina.forward(25)
    tina.left(90)

tina.penup()
tina.goto(0, 0)
tina.pendown()

tina.left(180)
tina.forward(200)

# make a stair case
for i in range(5):
    tina.forward(25)
    tina.left(90)
    tina.forward(25)
    tina.right(90)

tina.penup()
tina.goto(0, 80)
tina.pendown()

# Draw a square spiral
for i in range(20):
    tina.forward(10*i)
    tina.right(90)  

tina.penup()
tina.goto(10, 227)
tina.pendown()


# Draw a triangle spiral
for i in range(20):
    tina.forward(10*i)
    tina.right(120)




turtle.done()