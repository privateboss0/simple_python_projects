import turtle
from turtle import *

t = turtle.Turtle()
t.speed(0)

#Draw the Green heart
t.color("Green")
t.begin_fill()
t.pensize(3)
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()

t.penup()
t.setheading(0)  # Set the turtle's heading to 0 degrees
t.goto(-270, 0)
t.pendown()

#Draw the Red heart
t.color("Red")
t.begin_fill()
t.pensize(3)
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()

t.penup()
t.setheading(0)  # Set the turtle's heading to 0 degrees
t.goto(270, 0)
t.pendown()

#Draw the Blue heart
t.color("Blue")
t.begin_fill()
t.pensize(3)
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()
turtle.Screen().mainloop()