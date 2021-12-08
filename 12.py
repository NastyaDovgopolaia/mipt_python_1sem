import turtle
import math

def crcl(R):
    for i in range(360):
        turtle.forward(math.pi * (R/180))
        turtle.left(1)

def arc(R):
    for i in range(180):
        turtle.forward(math.pi * (R/180))
        turtle.right(1)

turtle.speed(0)
turtle.shape('turtle')

turtle.color("yellow")
turtle.goto(0, 0)
turtle.begin_fill()
crcl(100)
turtle.end_fill()

turtle.penup()
turtle.goto(-60, 80)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
crcl(20)
turtle.end_fill()

turtle.penup()
turtle.goto(60, 80)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
crcl(20)
turtle.end_fill()

turtle.penup()
turtle.goto(-60, 83)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
crcl(17)
turtle.end_fill()
