import turtle

jo = turtle.Turtle()
jo.color("green")
jo.speed(10)
jo.shape("turtle")
jo.width(4)

# make a stair case
for i in range(36):
    jo.forward(25)
    jo.right(90)
    jo.forward(25)  
    jo.left(90)

jo.penup()
jo.goto(0, 0)
jo.pendown()
# Draw a square spiral

for i in range(20): 
    
    jo.forward(100)
    jo.right(90)

jo.penup()
jo.goto(50, 50)
jo.pendown()


for banana in range(10):
    for i in range(6):
        jo.forward(10*banana)
        jo.left(60)

    jo.penup()
    jo.goto(jo.xcor() +10,jo.ycor())
    jo.pendown()


turtle.done()