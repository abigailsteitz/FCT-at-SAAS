import turtle
import math

def draw_spiral_triangles(t, center, size, levels, color, angle=0):
    # Draw a square spiral
    t.setheading(180) # face west
    t.penup()
    t.goto(-0, 145) # x left right, y up down
    t.pendown()

    for i in range(20):    
        t.forward(10*i)
        t.right(120)  

def draw_expanding_squares(t, center, size, levels, color):
    """Draw expanding nested squares with the largest square determining the triangle base."""
    if levels == 0:
        return
    t.penup()
    t.goto(center[0] - size / 2, center[1] - size / 2)
    t.pendown()
    t.pencolor(color)
    for _ in range(4):
        t.forward(size)
        t.left(90)
    draw_expanding_squares(t, center, size * 1.3, levels - 1, color)

def draw_steps(t, start_x, start_y, step_size, steps, color):
    """Draw step-like structure leading up to the bottom of the largest square."""
    t.penup()
    t.goto(-140, -200)
    t.pendown()
    t.pencolor(color)
    for _ in range(steps):
        t.forward(step_size)
        t.left(90)
        t.forward(step_size)
        t.right(90)
    for _ in range(steps):
        t.forward(step_size)
        t.right(90)
        t.forward(step_size)
        t.left(90)

t = turtle.Turtle()
t.speed(0)

# Define base sizes to scale
initial_square_size = 50
max_square_size = initial_square_size * (1.3 ** 6)  # Largest square size after recursion
triangle_size = max_square_size  # Triangle base matches largest square width
step_size = initial_square_size / 2

# Adjust positions so the shapes touch properly
square_center = (0, 0)
square_top_y = square_center[1] + max_square_size / 2

draw_steps(t, -max_square_size / 2, -max_square_size - step_size * 5, step_size, 5, 'green')
draw_expanding_squares(t, square_center, initial_square_size, 6, 'red')
draw_spiral_triangles(t, (0, square_top_y), triangle_size, 6, 'blue')

turtle.done()
