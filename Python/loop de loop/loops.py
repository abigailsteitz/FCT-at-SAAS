import turtle

jo = turtle.Turtle()

jo.penup()
jo.forward(100)
jo.pendown()

# Draw a square
for i in range(4):
    jo.forward(100)
    jo.right(90)

jo.penup()
jo.goto(-50,50)
jo.pendown()

# Draw a triangle 
for i in range(3):
    jo.forward(100)
    jo.right(120)

jo.penup()
jo.goto(-205,205)
jo.pendown()

# Draw a rectangle
for i in range(2):
    jo.forward(100)
    jo.right(90)
    jo.forward(150)
    jo.right(90)

jo.penup()
jo.goto(-300,300)
jo.pendown()

    #Draw a dimond
for i in range(2):
    jo.forward(120)
    jo.right(120)
    jo.forward(120)
    jo.right(60)

jo.penup()
jo.goto(-400,100)
jo.pendown()

for i in range(7):
    jo.forward(100)
    jo.right(51.5)

turtle.done()