import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Display JPG with Turtle Graphics")

# Specify the path to your JPG file
image_path = "Python/Text Adventure/tiger.gif"  # Replace with the path to your JPG file

# Set the background image
screen.bgpic(image_path)

# Keep the window open until the user closes it
screen.mainloop()