import turtle

a0 = [0, 0, 50, 0, 0, -100, -50, 0, 0, 100, 0, 0]
a1 = [0, -50, 50, 50, 0, -100, -50, 100]
a2 = [0, 0, 50, 0, 0, -50, -50, -50, 50, 0, -50, 100]
a3 = [0, 0, 50, 0, -50, -50, 50, 0, -50, -50, 0, 100]
a4 = [0, 0, 0, -50, 50, 0, 0, -50, 0, 100, -50, 0]
a5 = [50, 0, -50, 0, 0, -50, 50, 0, 0, -50, -50, 0, 0, 100]
a6 = [50, 0, -50, -50, 0, -50, 50, 0, 0, 50, -50, 0, 0, 50]
a7 = [0, 0, 50, 0, -40, -50, 0, -50, 0, 100]
a8 = [0, 0, 50, 0, 0, -50, -50, 0, 0, -50, 50, 0, 0, 50, -50, 0, 0, 50, 0, 0]
a9 = [0, -100, 50, 50, 0, 50, -50, 0, 0, -50, 50, 0, -50, 50]

ak = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]

def numb(a):
    x = turtle.xcor()
    y = turtle.ycor()
    for k in range(0, len(a), 2):
        if (k == 0) or (k == len(a) - 2):
            x += a[k]
            y += a[k + 1]
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
        else:
            x += a[k]
            y += a[k + 1]
            turtle.goto(x, y)


x = -200
y = 0
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
#(number 141700)
i = [1, 4, 1, 7, 0, 0]
for j in i:
    numb(ak[j])
    x = turtle.xcor()
    y = turtle.ycor()
    turtle.penup()
    turtle.goto(x + 100, y)
    turtle.pendown()
turtle.exitonclick()
