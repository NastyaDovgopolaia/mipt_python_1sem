import turtle
turtle.shape('turtle')
n=float(input()) 
i=360/n
while i<361:
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.right(360/n)
    i=+1
