import turtle

# for i in range(__) is a loop that will run the code inside the loop __ times
# purr.penup() will lift the pen up so the turtle will not draw
# purr.goto(__,__ ) will move the turtle to the x and y coordinates
# purr.pendown() will put the pen down so the turtle will draw

purr = turtle.Turtle()

purr.penup()
purr.goto(50, 0)
purr.pendown()

purr.right(155)

# face outline
for i in range(2):
    purr.forward(100)
    purr.right(50)
    purr.forward(100)
    purr.right(130)
   
# Ears
purr.right(115)

for i in range(2):
    purr.forward(120)
    purr.left(132.5)
    purr.forward(118)
    purr.penup()
    purr.goto(-47, 41)
    purr.pendown()
    purr.right(80)

#Feet
purr.penup()
purr.goto(50, 0)
purr.pendown() 
purr.right(-75)

# Right foot
purr.forward(230)
purr.right(100)
purr.forward(90)
purr.right(80)
purr.forward(173)

purr.penup()
purr.goto(-130,0)
purr.pendown()

# Left foot
purr.right(180)
purr.forward(230)
purr.left(103)
purr.forward(93)

# Tail
purr.penup()
purr.goto(50,-200)
purr.pendown()

purr.forward(45)
# 80
purr.penup()
purr.goto(130,-176)
purr.pendown()

purr.left(75)
purr.forward(80)
purr.left(60)
purr.forward(96)

# Tip of tail
purr.backward(96)
purr.left(100)
purr.forward(120)
purr.left(150)
purr.forward(56)

# Eyes
purr.penup()
purr.goto(-15,8) 
purr.pendown()

purr.right(130)

# Right eye
for i in range(17):
    purr.left(1)
    purr.forward(2)
    purr.dot(5)
    purr.backward(1)
    purr.right(1)

# Left eye
purr.penup()
purr.goto(-72,8)
purr.pendown()

for i in range(17):
    purr.left(1)
    purr.forward(2)
    purr.dot(5)
    purr.backward(1)
    purr.right(1)

# Nose
purr.penup()
purr.goto(-40,-34)

turtle.done()