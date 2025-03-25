import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("snow")
colors = ["snow", "darkolivegreen", "firebrick", "purple", "navy", "darkseagreen"]
t.pensize(2)
t.speed(10)

for x in range(500):
    def curve():
      for i in range(360):
            t.pencolor(colors[(i // 10) % len(colors)]) 
            t.right(1)
            t.forward(1)
    t.left(120)
    curve()
    t.forward(x)
    t.end_fill()
    t.hideturtle()
        
t.penup()

t.goto(40, 40)

t.pendown ()

turtle.mainloop()

