import turtle
from turtle import *

t = turtle.Turtle()
t.speed(0)

#Draw the White heart
t.color("White")
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

#Draw the Silver heart
t.color("Silver")
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

#Draw the Orange heart
t.color("Orange")
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