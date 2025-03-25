import turtle

jo = turtle.Turtle()

jo.forward(100)

# Draw a square
for i in range(4):
    jo.forward(100)
    jo.right(90)

jo.penup()
jo.goto(200,200)
jo.pendown()

# Draw a triangle
for i in range(3):
    jo.forward(100)
    jo.right(120)

jo.penup()
jo.goto(-200,200)
jo.pendown()

for i in range(6):
    jo.forward(80)
    jo.right(60)

jo.circle(50,180)
jo.penup()
jo.goto(-200,-200)
jo.pendown()
turtle.color("blue")

for i in range(5):
    jo.forward(50)
    jo.right(72)

jo.penup()
jo.goto(0,-200)
jo.pendown()

for i in range(10):
    jo.forward(40)
    jo.right(36)


turtle.done()

