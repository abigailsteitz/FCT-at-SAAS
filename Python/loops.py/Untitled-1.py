import turtle


lebronjames = turtle.Turtle()
lebronjames.color("green")
lebronjames.speed(10)
lebronjames.shape("turtle")
lebronjames.width(4)

for i in range(5):
    lebronjames.forward(25)
    lebronjames.left(90)
    lebronjames.forward(25)
    lebronjames.right(90)
    
for i in range(5):
 lebronjames.forward(50)
for i in range(5):
    lebronjames.forward(25)
    lebronjames.right(90)
    lebronjames.forward(25)
    lebronjames.left(90)

lebronjames.penup()
lebronjames.goto(150, 125)
lebronjames.pendown()

# draw concetric squares
for banana in range(5):
   for i in range (6):
        lebronjames.forward(10*banana)
        lebronjames.left(90)


    
turtle.done()