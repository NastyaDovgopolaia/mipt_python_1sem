import turtle
turtle.shape('turtle')
for i in range(10,200,20):
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90) 
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.pendown()
