import turtle

# Setup
tina = turtle.Turtle()
tina.speed(0)
tina.width(1)
tina.hideturtle()

# --- Constants ---
step = 10
square_count = 10
triangle_count = 10
hill_steps = 10
square_size = step * square_count * 2  # 200
roof_height = square_size
square_bottom_y = -square_size / 2

# --- Draw Hill with Flat Top Slightly Below the Square ---
tina.penup()
tina.color("green")

# Lower the hill by one step for visual gap
hill_top_y = square_bottom_y - step
hill_start_y = hill_top_y - hill_steps * step
hill_start_x = -square_size / 2 - hill_steps * step

tina.goto(hill_start_x, hill_start_y)
tina.setheading(0)
tina.pendown()

# Left staircase up
for _ in range(hill_steps):
    tina.forward(step)
    tina.left(90)
    tina.forward(step)
    tina.right(90)

# Flat top (just *below* the square)
tina.forward(square_size)

# Right staircase down
for _ in range(hill_steps):
    tina.forward(step)
    tina.right(90)
    tina.forward(step)
    tina.left(90)

# --- Draw Nested Squares (Red Body) ---
tina.penup()
tina.color("red")
tina.goto(-square_size / 2, square_bottom_y)
tina.setheading(0)
tina.pendown()

for i in range(square_count):
    offset = i * step
    side = square_size - 2 * offset
    tina.penup()
    tina.goto(-side / 2, square_bottom_y + offset)
    tina.setheading(0)
    tina.pendown()
    for _ in range(4):
        tina.forward(side)
        tina.left(90)
# --- Draw Triangular Spiral (Blue Pen) ---
tina.penup()
tina.color("blue")
tina.goto(0, 160)  # Center of the square, shifted 50 points higher
tina.setheading(0)
tina.pendown()

length = 10
for _ in range(100):  # Adjust the range for desired spiral size
    tina.forward(length)
    tina.left(120)  # Turn to form a triangle
    length += 2  # Increment the side length for the spiral effect

# --- Draw Tight Spiral in Top Right Corner ---
tina.penup()
tina.color("purple")

# Place near top-right of the roof
spiral_center_x = square_size / 2 + 100
spiral_center_y = square_size / 2 + roof_height + 50
tina.goto(spiral_center_x, spiral_center_y)
tina.setheading(0)
tina.pendown()

# Extremely tight and smooth spiral
radius = 1
while radius < 100:
    tina.circle(radius, 2)
    radius += 0.05

turtle.done()
