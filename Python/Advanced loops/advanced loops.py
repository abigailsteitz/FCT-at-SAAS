import turtle


alice = turtle.Turtle()
alice.color("red")
alice.speed(6)
alice.shape("turtle")
alice.width(3)

alice.penup()
alice.goto(-100,-50)
alice.pendown()

for _ in range(3):
    alice.forward(25)
    alice.left(90)
    alice.forward(25)
    alice.right(90)

alice.forward(200)

for _ in range(3):
    alice.forward(25)
    alice.right(90)
    alice.forward(25)
    alice.left(90)
alice.right

alice.penup()
alice.goto(100, 200)
alice.pendown()

for i in range(1, 25):
    alice.forward(-10 * i)
    alice.right(120)

alice.penup()
alice.goto(100, 100)
alice.pendown()

for banana in range(10):
    for i in range(4): 
        alice.forward(10 * (banana + 1))
        alice.left(90)

    alice.penup()  
    alice.goto(alice.xcor() -5, alice.ycor() -5)
    alice.pendown() 


turtle.done()
