import turtle as t

dt = 0
ay = -10
Vx = 20
Vy = 40
x = -300
y = 0
k = 0
i = 0

t.penup()
t.goto(x, y)
t.pendown()

while i < 11:
    while y >= 0:
        k += 1
        dt = k / 10000
        x += Vx*dt
        y += Vy*dt + ay*dt**2/2
        Vy += ay*dt
        if y >= 0:
            t.goto(x, y)
        else:
            t.goto(x, 0)
    Vx = 0.8 * Vx
    Vy = abs(0.8 * Vy)
    y = 0
    i += 1
t.exitonclick()
