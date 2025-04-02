import turtle
joe = turtle.Turtle()
joe.forward(100) 
for i in range(100):
    joe.forward(10)
    joe.right(10)

joe.penup()
joe.goto(-100, 0)
joe.pendown()


for i in range(10):
    joe.forward(50)
    joe.right(40)
joe.penup()
joe.goto(-100, 0)
joe.pendown()

for i in range(5):
    joe.forward(50)
    joe.right(144)
joe.penup()
joe.goto(-100, 0)
joe.pendown()

turtle.done()
