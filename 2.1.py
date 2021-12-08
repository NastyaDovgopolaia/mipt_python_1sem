import turtle
from random import *

turtle.speed(10)
for i in range(1000):
    turtle.left(randint(0, 360))
    turtle.forward(randint(1, 100))
turtle.exitonclick()
