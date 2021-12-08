
import math
import turtle

def myg(x, y):
	k = 0
	x = int(x)
	alf = math.radians(360/x)
	sin = math.sin(alf/2)
	a = 2 * y * sin
	alf1 = 180 * (x-2) / (2*x)
	alf2 = 180 - alf1*2
	turtle.shape('turtle')
	turtle.left(alf1 + alf2)
	while (k < x):
		turtle.forward(a)
		turtle.left(alf2)
		k += 1
	turtle.right(alf1 + alf2)

n = 3
R = 50
while (n < 14):
	myg(n, R)
	turtle.penup()
	turtle.forward(50)
	turtle.pendown()
	n += 1
	R += 50
turtle.exitonclick()


