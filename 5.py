import turtle
turtle.shape('turtle')
k=float(input())
turtle.forward(k)
turtle.left(90)
for i in range(2,1000,1):
    turtle.forward(k*i)
    turtle.left(90)
    turtle.forward(k*i)
    turtle.left(90)
    i+=1 
