import turtle
jo = turtle.Turtle()

# Draw a tutrle
jo.pencolor("green")
jo.circle(100)
jo.left(180)
jo.circle(50)
jo.penup()
jo.goto(110,30)
jo.right(180)
jo.pendown()
jo.circle(20)
jo.penup()
jo.goto(-110,30)
jo.pendown()
jo.circle(20)
jo.penup()
jo.goto(-98,150)
jo.pendown()
jo.circle(20)
jo.penup()
jo.goto(98,150)
jo.pendown()
jo.circle(20)
jo.penup()
jo.goto(0,200)
jo.pendown()
jo.circle(10)
jo.penup()

#draw an heart
jo.penup()
jo.goto(-250, -100)  # Adjusted x-coordinate to move it left
jo.pendown()
jo.pencolor("red")
jo.fillcolor("red")
jo.begin_fill()
jo.left(50)
jo.forward(100)  # Reduce the size
jo.circle(50, 180)  # Smaller semicircles
jo.right(90)
jo.circle(50, 180)
jo.forward(100)
jo.end_fill()
jo.penup()

#draw an interesting hexagon
jo.goto(300,-100)
jo.pendown()
jo.pencolor("purple")
for i in range(20):
    jo.forward(50)
    jo.right(59)

turtle.done()