import turtle
import math

def crcl(R, k):
    for i in range(360):
        turtle.forward(math.pi * (R/180))
        if k == 0:
            turtle.left(1)
        else:
            turtle.right(1)

turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
for R in range(50, 100, 10):
    crcl(R, 0)
    crcl(R, 1)
turtle.exitonclick()
