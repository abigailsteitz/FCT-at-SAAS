import turtle
#her name is shelly
shelly = turtle.Turtle()
shelly.penup()

shelly.goto(200,-100)
shelly.right(180)
shelly.pendown()
for i in range(4):
    shelly.forward(100)
    shelly.right(90)

#shelly likes sqaure

shelly.penup()
shelly.goto(-200,-100)
shelly.pendown()
for i in range(3):
    shelly.right(120)
    shelly.forward(100)


shelly.penup()
shelly.goto(-200,200)
shelly.pendown()
for i in range(5):
    shelly.right(72)
    shelly.forward(100)


shelly.penup()
shelly.goto(140,200)
shelly.pendown()
for i in range(8):
    shelly.right(45)
    shelly.forward(50)

shelly.penup()
shelly.goto(-80,-300)
shelly.pendown()
for i in range(400):
    shelly.right(1)
    shelly.forward(0.5)


shelly.penup()
shelly.goto(80,-300)
shelly.pendown()
for i in range(400):
    shelly.right(1)
    shelly.forward(0.5)

#shelly.penup()
#shelly.goto(-150,-350)
#shelly.right(140)
#shelly.pendown()
#for i in range(400):
    #shelly.left(0.02)
    #shelly.forward(1)



turtle.done()