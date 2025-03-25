import turtle 

nick = turtle.Turtle()
nick.speed(100000000000000000000000000000000000000000000000000000)
nick.penup()
nick.goto(-300,-300)
nick.pendown()


for i in range(6):
    nick.forward(100)
    nick.right(60)
nick.penup()
nick.goto(300,300)
nick.pendown()
for i in range(100):
    nick.forward(1)
    nick.right(3.6)


for i in range(20):
    nick.forward(10)
    nick.right(18)

for i in range(40): 
    nick.forward(10)
    nick.right(9)
for i in range(80): 
    nick.forward(10)
    nick.right(4.5)

nick.penup()
nick.goto(-300,300)
nick.pendown()

for i in range(1000000000000000):
    nick.forward(600)
    nick.right(89)


turtle.done()
