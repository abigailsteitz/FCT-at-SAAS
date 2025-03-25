import turtle

jeremy = turtle.Turtle()

jeremy.forward(100)


# Draw a circle
turtle.home()
turtle.position()
(0.00,0.00)
turtle.heading()
0.0
turtle.circle(50)
turtle.position()
(-0.00,0.00)
turtle.heading()
0.0

jeremy.penup()
jeremy.goto(-50,50)
jeremy.pendown()

# Draw a triangle
for i in range(36):
    jeremy.forward(70)
    jeremy.right(100)

    #Draw a rectangle
jeremy.penup()
jeremy.goto(-100,100)
jeremy.pendown()
for i in range(36):
    jeremy.forward(50)
    jeremy.right(90)
    jeremy.forward(20)
    jeremy.right(90)

