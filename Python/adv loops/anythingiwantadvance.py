import turtle
t=turtle.Pen()
t.speed(10)

#make a triangle
t.pencolor('blue')
t.penup()
t.goto(0,200)
t.width(2)
t.pendown()

for x in range(22):
    t.forward(x*10)
    t.left(120)

#make a square
t.penup()
t.goto(0,35)
t.pendown()
t.left(60)
t.pencolor ("red")

for x in range(11):
    for penguin in range(4):
        t.forward(x*20)
        t.right(90)

    t.penup()
    t.goto(t.xcor()+10,t.ycor()-10)
    t.pendown()




#make a staircase
t.penup()
t.goto(t.xcor()-350,t.ycor()-120)
t.pendown()
t.setheading(0)
t.pendown()
t.pencolor ("green")
for i in range(5):
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(25)

t.goto(t.xcor()+250,t.ycor()-0)

for i in range(5):
    t.right(90)
    t.forward(25)
    t.left(90)
    t.forward(25)