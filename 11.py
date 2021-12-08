import turtle
import math

def arc(R):
    for i in range(180):
        turtle.forward(math.pi * (R/180))
        turtle.right(1)

turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
for i in range(1, 4):
    arc(50)
    arc(10)
turtle.exitonclick()
