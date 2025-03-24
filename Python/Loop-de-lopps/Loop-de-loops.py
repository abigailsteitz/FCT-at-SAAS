import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Etch-A-Sketch with WASD + Arrow Keys")

# Create turtle
etcher = turtle.Turtle()
etcher.shape("turtle")
etcher.color("darkgreen")
etcher.pensize(3)
etcher.speed(0)

move_distance = 10  # pixels per move

# Movement functions
def up():
    etcher.setheading(90)
    etcher.forward(move_distance)

def down():
    etcher.setheading(270)
    etcher.forward(move_distance)

def left():
    etcher.setheading(180)
    etcher.forward(move_distance)

def right():
    etcher.setheading(0)
    etcher.forward(move_distance)

# Clear screen function
def clear_screen():
    etcher.clear()
    etcher.penup()
    etcher.home()
    etcher.pendown()

# Keyboard bindings
screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")
screen.onkeypress(clear_screen, "c")

turtle.done()