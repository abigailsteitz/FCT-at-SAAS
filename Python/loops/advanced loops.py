import turtle

shelly = turtle.Turtle()
shelly.speed(10)
shelly.shape("turtle")
shelly.width(5)

#STAIRCASE YIPPEEEE AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH be calm
shelly.color("green")
for i in range(10):
    shelly.forward(50)
    shelly.right(90)
    shelly.forward(50)
    shelly.left(90)

shelly.penup()
shelly.goto(0,0)
shelly.pendown()

#spiral square yeahhhhhh BOIIIIIII
#shelly.color("red")
#for i in range(25):
 #   shelly.forward(10*i+10)
  #  shelly.right(90)
for lily in range(10):
    for pizza in range(4):
        shelly.pendown()
        shelly.forward(10*lily+1)
        shelly.right(90)

    shelly.penup()
    shelly.goto(shelly.xcor() -1,shelly.ycor() +5)



#hexagon spiral :3 whatever

shelly.penup()
shelly.goto(0,-300)
shelly.color("pink")
shelly.pendown()
for fish in range(10):
    for i in range(6):
        shelly.pendown()
        shelly.forward(10*fish+1)
        shelly.right(60)


    shelly.penup()
    shelly.goto(shelly.xcor() +8,shelly.ycor() +5)


#TRIANGLE SPIRALLLLLLLL :D

shelly.penup()
shelly.goto(0,200)
shelly.color("blue")
shelly.right(60)
shelly.pendown()                                
for i in range(25):
    shelly.forward(10*i)
    shelly.right(120)









turtle.done()



