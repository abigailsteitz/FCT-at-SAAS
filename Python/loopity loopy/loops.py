import turtle

green= turtle.Turtle()

green.forward(100)



#draw a square
for i in range(4):
    green.forward(100)
    green.right(90) 

green.penup 
green.goto  (-200, 200)
green.pendown


# draw a friangle
for i in range(3):
    green.forward(100)
    green.right(120)


green.penup 
green.goto  (0,200)
green.pendown

# draw a half circle
for i in range(180):
    green.forward(1)
    green.right(1)
    green.right(1)
    green.forward(1)

#draw a rectangle

green.penup
green.goto  (-200, -200)  
green.pendown
for i in range(2):
    green.forward(200)
    green.right(90)
    green.forward(100)
    green.right(90)

#draw a pentagon
green.penup
green.goto  (200, -200)
green.pendown
for i in range(5):
    green.forward(100)
    green.right(72)
    

turtle.done()