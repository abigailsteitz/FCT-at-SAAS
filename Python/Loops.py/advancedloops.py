import turtle

Stevie = turtle.Turtle()
Stevie.color("green")
Stevie.speed(10)
Stevie.shape("turtle")
Stevie.width(4)

# move staircase
Stevie.penup()
Stevie.goto(90, -50)
Stevie.pendown()

# make a stair case
for i in range(10):
    Stevie.forward(25)
    Stevie.right(90)
    Stevie.forward(25)
    Stevie.left(90)

Stevie.penup()
Stevie.goto(-90, -50)
Stevie.pendown()

Stevie.setheading(180)

# make a stair case
for i in range(10):
    Stevie.forward(25)
    Stevie.left(90)
    Stevie.forward(25)
    Stevie.right(90)
    
Stevie.penup()
Stevie.goto(0, 120)
Stevie.pendown()

# Draw a square spiral
for i in range(20):
    Stevie.forward(10*i)
    Stevie.right(120)  

Stevie.penup()
Stevie.goto(0, 0)
Stevie.pendown()


Stevie.setheading(0)

# Draw a hexagonal concentric spiral
for banana in range(10):
    for i in range(4):
        Stevie.forward(10*banana)
        Stevie.left(90)

    Stevie.penup()
    Stevie.goto(Stevie.xcor() -5,Stevie.ycor()-5)
    Stevie.pendown()

turtle.done()