#Camryn Moschitta
#CS-175L

#stopSign

import math
import turtle

# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2*x)

# Initialize the turtle.

turtle.pensize(4)
turtle.color('Black')
turtle.fillcolor('#cf142b')
turtle.begin_fill()
turtle.penup()
turtle.setposition(-50,100)
for i in range(NUM_SIDES):
    turtle.pendown()
    turtle.forward(LENGTH)
    turtle.right(ANGLE)
    turtle.penup()
turtle.end_fill()

turtle.setposition(-98,-60)
turtle.color("White")
turtle.write("STOP", font=("Highway Gothic", 80), align=("left"))
turtle.hideturtle()

