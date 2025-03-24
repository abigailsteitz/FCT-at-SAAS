import turtle

bob = turtle.Turtle()

bob.forward(100)

# Draw a square
turtle.penup()
turtle.goto(-40,50)
turtle.pendown()

for i in range(4):
    bob.forward(100)
    bob.right(90)

turtle.hideturtle()

bob.penup()
bob.goto(-50,50)
bob.pendown()

import turtle
import turtle

bob = turtle.Turtle()

# Move the turtle to the right
bob.penup()
bob.goto(100, 0)
bob.pendown()

# Draw a triangle
for i in range(3):
    bob.forward(100)
    bob.left(120)

bob.hideturtle()  # Hide the turtle after drawing

# Draw a square
def draw_square(length):
    for _ in range(4):
        bob.forward(length)
        bob.right(90)

# Draw a triangle
def draw_triangle(length):
    for _ in range(3):
        bob.forward(length)
        bob.left(120)

# Draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        bob.forward(width)
        bob.left(90)
        bob.forward(height)
        bob.left(90)

# Draw a house (combination of square and triangle)
def draw_house():
    bob.speed(3)
    
    # Draw the base (square)
bob.penup()
bob.goto(-100, 100)  # Raise the base square by adjusting the Y-coordinate
bob.pendown()
draw_square(200)
    
    # Draw the roof (triangle)
bob.penup()
bob.goto(-100, 100)
bob.pendown()
draw_triangle(200)
    
    # Draw the door (rectangle)
bob.penup()
bob.goto(-30, -100)
bob.pendown()
draw_rectangle(60, 100)
    
    # Draw windows (squares)
bob.penup()
bob.goto(-80, 20)
bob.pendown()
draw_square(40)
    
bob.penup()
bob.goto(40, 20)
bob.pendown()
draw_square(40)

# Draw a castle (rectangle and battlements)
def draw_castle():
    bob.penup()
    bob.goto(-250, -100)
    bob.pendown()
    draw_rectangle(100, 300)  # Tall rectangle for castle body
    
    # Draw battlements (rectangles on top)
    bob.penup()
    bob.goto(-250, 200)
    bob.pendown()
    for _ in range(5):  # Draw 5 battlements
        draw_rectangle(20, 20)
        bob.forward(20)

# Draw everything
draw_house()
draw_castle()

bob.hideturtle()
turtle.done()
