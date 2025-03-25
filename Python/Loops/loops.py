import turtle

myles = turtle.Turtle()



for i in range (6):
    myles.forward(100)
    myles.right(60)


myles.penup()
myles.goto(200,200)
myles.pendown()



for i in range (9):
    myles.forward(100)
    myles.right(40)


myles.penup()
myles.goto(-70,-70)
myles.pendown()


radius = 100
myles.circle(radius)


turtle.done()



