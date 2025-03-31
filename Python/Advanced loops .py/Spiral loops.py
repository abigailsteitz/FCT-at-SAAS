import turtle
# this assignment is to copy an image made by my teacher

# Settings
purr = turtle.Turtle()
purr.color("green")
purr.speed(7)
purr.width(3)

# Stairs
purr.penup()
purr.goto(-315, -360)
purr.pendown()

for i in range(5):
    purr.left(90)
    purr.forward(27)
    purr.right(90)
    purr.forward(27)

purr.forward(370)

for i in range(5):
    purr.right(90)
    purr.forward(27)
    purr.left(90)
    purr.forward(27)

# Box
purr.color("red")
purr.penup()
purr.goto(0, -99)
purr.pendown()

for kit in range(10):
        for i in range(4):
            purr.forward(28*kit)
            purr.right(90)
        purr.penup()
        purr.goto(purr.xcor() -14, purr.ycor() + 14)
        purr.pendown()

# Triangle
purr.color("blue")
purr.penup()
purr.goto(0, 105)    
purr.pendown()
purr.left(120)

for i in range(20):  
    purr.forward(15*i)
    purr.left(120)

# Circle 
purr.color("yellow")
purr.penup()
purr.goto(-250, 250)
purr.pendown()

radius = 1 * 3.14
angle = 10
increase = 1 * 3.14

for i in range(40):
    purr.circle(radius, angle)
    radius += increase
    angle += 1 * 3.14

turtle.done()

