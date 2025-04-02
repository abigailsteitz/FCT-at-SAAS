import turtle

tina = turtle.Turtle()
tina.color("green")
tina.speed(10)
tina.shape("turtle")
tina.width(4)

# make a stair case
for i in range(10):
    tina.forward(40)
    tina.right(90)
    tina.forward(25)
    tina.left(90)

tina.penup()
tina.goto(0, 0)
tina.pendown()


# make a stair case
for i in range(10):
    tina.backward(40)
    tina.right(90)
    tina.forward(25)
    tina.left(90)

tina.penup()
tina.goto(0, 0)
tina.pendown()


# Draw a nested square spiral
for i in range(20):
    tina.forward(10*i)
    tina.right(90)  

tina.penup()
tina.goto(50, 50)
tina.pendown()


#draw triangle






