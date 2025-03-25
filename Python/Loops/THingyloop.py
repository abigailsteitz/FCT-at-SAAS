import turtle
import math

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("snow")
colors = ["snow", "darkolivegreen", "firebrick", "purple", "navy", "darkseagreen"]
t.pensize(2)
t.speed("fastest")


def draw_spike():
    for i in range(5):
        t.forward(100)
        t.right(144)
        t.forward(100)
        t.left(72 + i)

def draw_great_stellated_dodecahedron():
    for i in range(1270):
        t.pencolor(colors[i % len(colors)])
        draw_spike()
        t.right(360 / 12)

t.penup()
t.goto(0, -50)
t.pendown()

draw_great_stellated_dodecahedron()

t.hideturtle()
turtle.mainloop()