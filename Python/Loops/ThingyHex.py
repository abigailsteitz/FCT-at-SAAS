import turtle
import math

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("snow")
colors = ["snow", "darkolivegreen", "firebrick", "purple", "navy", "darkseagreen"]
t.pensize(2)
t.speed("fastest")

def draw_eight_pointed_star():
    for i in range(8):
        t.forward(100)
        t.right(135)

def draw_pattern():
    for i in range(1200):
        t.pencolor(colors[i % len(colors)])
        draw_eight_pointed_star()
        t.right(360 / 12)

t.penup()
t.goto(0, -50)
t.pendown()

draw_pattern()

t.hideturtle()
turtle.mainloop()