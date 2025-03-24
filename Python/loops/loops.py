import turtle 

birdie = turtle.Turtle()

birdie.forward(100)


# Draw a square
for i in range (4):
    birdie.forward(100)
    birdie.right(90)

birdie.penup()
birdie.goto(-50,50)
birdie.pendown()

# Draw a triangle
for i in range(3):
    birdie.forward(100)
    birdie.right(120)

birdie.penup()
birdie.goto(-70,70)
birdie.pendown()

# Draw a hexagon
for i in range(6):
    birdie.fd(8)
    birdie.left(300)

birdie.penup()
birdie.goto(-80,80)
birdie.pendown()

# Draw a decagon
for i in range(10):
    birdie.fd(10)
    birdie.left(36)

birdie.penup()
birdie.goto(-100,100)
birdie.pendown()

# Draw a octogon
for i in range(8):
    birdie.fd(10)
    birdie.left(45)


turtle.done()