import turtle
from turtle import *

def draw_heart(color):
    t.color(color)
    t.begin_fill()
    t.pensize(3)
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()

t = turtle.Turtle()
t.speed(0)

# Draw the pink heart
draw_heart("Pink")

# Move the turtle to the position for the red heart
t.penup()
t.setheading(0)
t.goto(-270, 0)
t.pendown()

# Draw the Black heart
draw_heart("Black")

# Move the turtle to the position for the blue heart
t.penup()
t.setheading(0)
t.goto(270, 0)
t.pendown()

# Draw the Yellow heart
draw_heart("yellow")

turtle.Screen().mainloop()