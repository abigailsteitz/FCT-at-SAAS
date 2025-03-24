import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Turtle Drawing Request")

pen = turtle.Turtle()
pen.speed(0)

# Drawing: Circle Flower 🌸
def draw_circle_flower():
    pen.color("hotpink")
    for _ in range(36):  # loop to make petals
        pen.circle(100)
        pen.left(10)

# Drawing: Star ⭐
def draw_star():
    pen.color("gold")
    pen.begin_fill()
    for _ in range(5):  # loop for 5 star points
        pen.forward(100)
        pen.right(144)
    pen.end_fill()

# Drawing: Spiral 🔄
def draw_spiral():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(100):  # loop for spiral
        pen.color(colors[i % 6])
        pen.forward(i * 2)
        pen.left(59)

# Ask the user
shape = screen.textinput("Pick a Shape", "Type one: circle_flower, star, spiral").lower()

# Clear before drawing
pen.clear()

# Match user input
if shape == "circle_flower":
    draw_circle_flower()
elif shape == "star":
    draw_star()
elif shape == "spiral":
    draw_spiral()
else:
    pen.color("red")
    pen.write("Unknown shape!", font=("Arial", 16, "bold"))

pen.hideturtle()
turtle.done()
