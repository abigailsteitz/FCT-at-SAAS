import turtle

jo = turtle.Turtle()

jo.forward(100)

# Draw a square
for i in range(4):
    jo.forward(100)
    jo.right(20)

jo.penup()
jo.goto(-50,50)
jo.pendown()

# Draw a triangle
for i in range(3):
    jo.forward(100)
    jo.right(20)

turtle.done()