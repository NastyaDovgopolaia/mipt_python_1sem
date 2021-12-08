import turtle
import math

def crcl(R):
    for i in range(360):
        turtle.forward(math.pi * (R/180))
        turtle.left(1)

turtle.shape('turtle')
turtle.speed(0)
for n in range(1, 7):
    crcl(50)
    turtle.left(60)
turtle.exitonclick()
