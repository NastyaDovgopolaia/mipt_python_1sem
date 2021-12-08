import turtle
turtle.shape('turtle')
for i in range(1,360,1): 
    turtle.forward(1+i-i)
    turtle.left(i+1-i)
    
