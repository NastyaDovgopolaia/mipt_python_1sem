import turtle
import math

def star(n):
    turtle.left(180)
    ang = 180-(180/n)
    for i in range(1, n+1):
        turtle.forward(100)
        turtle.left(ang)

turtle.shape('turtle')

turtle.penup()
turtle.goto(-20, 0)
turtle.pendown()
star(5)

turtle.penup()
turtle.goto(90, 0)
turtle.pendown()
star(11)
turtle.exitonclick()
