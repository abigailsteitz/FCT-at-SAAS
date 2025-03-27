import turtle

jit = turtle.Turtle()
jit.color("blue")
jit.speed(10)
jit.shape("turtle")
jit.width(2)
jit.penup()
jit.goto(0,200)
jit.pendown()

for i in range (22):
    jit.left(120)
    jit.forward(10*i)

jit.penup()
jit.goto(0,30)
jit.pendown()
jit.color("red")
jit.right(30)
for sqrsize in range (10):
    for i in range(4):
        jit.forward(20*sqrsize)
        jit.right(90)
    
    jit.penup()
    jit.goto(jit.xcor() -10,jit.ycor() -10)
    jit.pendown()

jit.penup()
jit.goto(0,-80)
jit.pendown()
jit.color("green")
jit.right(90)
jit.forward(100)

for i in range (5):
    jit.right(90)
    jit.forward(10)
    jit.left(90)
    jit.forward(10)

jit.penup()
jit.goto(0,-80)
jit.pendown()
jit.left(180)
jit.forward(100)

for i in range (5):
    jit.left(90)
    jit.forward(10)
    jit.right(90)
    jit.forward(10)

turtle.done()