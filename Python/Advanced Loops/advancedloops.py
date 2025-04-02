
import turtle

# Removed unused import as "network" module is not available

Jeff = turtle.Turtle()
Jeff.color("green")
Jeff.speed(10)
Jeff.shape("turtle")
Jeff.width(5)

Jeff.penup()
Jeff.goto(125, 0)
Jeff.pendown()

for i in range(5):
    Jeff.forward(25)
    Jeff.right(90)
    Jeff.forward(25)
    Jeff.left(90)

Jeff.penup()
Jeff.goto(125, 0)
Jeff.pendown()

Jeff.left(180)
Jeff.forward(300)

for i in range(5):
    Jeff.forward(25)
    Jeff.left(90)
    Jeff.forward(25)
    Jeff.right(90)


Jeff.penup()
Jeff.goto(-30, 100)
Jeff.pendown()

Jeff.pencolor("red")

side_length = 20 # Initial side length
increment = 10   # Amount to increase the side length each iteration
for i in range(10):
        for _ in range(4):
            Jeff.forward((i * 10))
            Jeff.right(90)
        Jeff.penup()
        Jeff.goto(Jeff.xcor() +4, Jeff.ycor() -3) # Move to the next square position
        Jeff.pendown()

Jeff.penup()
Jeff.goto(-25, 275)
Jeff.pendown()

Jeff.pencolor("blue")


side_length = 20  # Initial side length
increment = 10    # Amount to increase the side length each iteration

for i in range(20):  # Number of iterations
    Jeff.forward(side_length)  # Draw one side of the square
    Jeff.right(120)  # Turn 90 degrees to form the corner
    side_length += increment 



turtle.done()
