import turtle

bob = turtle.Turtle()
bob.color("red")
bob.speed(10)
bob.shape("turtle")
bob.width(1)


# Drawing a square 
for orange in range(10):
    for i in range(4):
        bob.forward(10*orange)
        bob.right(90)  
    bob.penup()
    bob.goto(bob.xcor() - 5,bob.ycor() + 5)
    bob.pendown()

bob.penup()
bob.goto(0, 75)
bob.pendown()

bob.setheading(0)

# Drawing a triangle thingy
bob.color("blue")
for i in range(14):
    bob.forward(7*i)
    bob.left(120)   

#green thingy
bob.penup()
bob.goto(-112.5, -112.5)
bob.pendown()
bob.color("green")
bob.setheading(0)
bob.left(90)

for i in range(5):
    bob.forward(12.5)
    bob.right(90)
    bob.forward(12.5)
    bob.left(90)
bob.right(90)
bob.forward(95)
for i in range(5):
    bob.forward(12.5)
    bob.right(90)
    bob.forward(12.5)
    bob.left(90)

turtle.done()