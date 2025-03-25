import turtle
colors=['midnightblue','mediumblue','royalblue','cornflowerblue','lightsteelblue', 'azure']
t=turtle.Pen()
t.speed(10)
t.penup()
t.goto(-210,100)
t.pendown()
turtle.bgcolor('black')
for x in range(18):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    for x in range(12):
        t.forward(2*x)
        t.left(40)
    t.forward(5*x)
    t.left(120)
    t.forward(x)
    t.left(100)

t.penup()
t.goto(200,200)
t.pendown()
t.pencolor('darkseagreen')
for x in range(50):
    t.forward(100)
    t.right(144.5)


t.penup()
t.goto(70,-70)
t.pendown()
t.pencolor('darkred')

for x in range(720):
    t.forward(300)
    t.right(121)
