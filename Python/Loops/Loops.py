import turtle

bella = turtle.Turtle()

bella.forward(100)

# Draw a square
for i in range(4):
    bella.foward(100)
    bella.right(90)

bella.penup()
bella.goto(-50,50)
bella.pendown()

# Draw a triangle
for i in range(3):
    bella.foward(100)
    bella.right(120)

turtle.done()
