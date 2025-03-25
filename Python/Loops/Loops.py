import turtle

bob = turtle.Turtle()


for i in range(360):
    bob.forward(1)
    bob.right(1)

bob.penup()
bob.goto(150,60)
bob.pendown()

for i in range(6):
    bob.forward(100)
    bob.right(60)

bob.penup()
bob.goto(-200,300)
bob.pendown()

for i in range(10):
    bob.forward(80)
    bob.right(36)

turtle.done()