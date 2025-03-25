import turtle

Turt = turtle.Turtle()


      
turtle.home()
turtle.position()
(0.00,0.00)
turtle.heading()
0.0
turtle.circle(50)
turtle.position()
(-0.00,0.00)
turtle.heading()
0.0

Turt.penup()
Turt.goto(-50,-50)
Turt.pendown()

for i in range(6):
    Turt.forward(100)
    Turt.right(60)

Turt.penup()
Turt.goto(50,150)
Turt.pendown()

for i in range(8):
    Turt.forward(25)
    Turt.left(45)
    



turtle.done()