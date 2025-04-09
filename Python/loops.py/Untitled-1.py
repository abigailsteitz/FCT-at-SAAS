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
lebronjames.goto(260, 250)
lebronjames.pendown()

# draw concetric squares
for banana in range(25):
    for i in range (4):
        lebronjames.forward(10*banana)
        lebronjames.left(90)
    lebronjames.penup()
    lebronjames.goto(lebronjames.xcor() -5,lebronjames.ycor()-5)
    lebronjames.pendown()

#draw spiral triangle
lebronjames.penup()
lebronjames.goto(260, 400)
lebronjames.pendown()

lebronjames.setheading(180)

for i in range(20):
   
    lebronjames.right(120) 
    lebronjames.forward(10*i) 

lebronjames.penup()
lebronjames.goto(50, 50)
lebronjames.pendown()
        
        




    
turtle.done()