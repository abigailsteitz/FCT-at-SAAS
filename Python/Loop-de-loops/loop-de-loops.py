import turtle

jo = turtle.Turtle()

# Class lecture example
# TODO: make this function take size as a paremeter
def squares(height):
  for i in range(4):
    jo.forward(height)
    jo.right(90)
  
  jo.penup()
  jo.goto(height/4, -height/4)
  jo.pendown()
  
  for i in range(4):
    jo.forward(height*0.5)
    jo.right(90)

squares(16)
turtle.done()