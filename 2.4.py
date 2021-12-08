import turtle as t

t0, g, v1, v2, x, y, i, j = 0, -10, 30, 60, -400, 0, 0, 0

t.penup()
t.goto(x, y)
t.pendown()

while j < 15:
    while y >= 0:
        i += 1
        t0 = i / 10000
        x += v1*t0
        y += v2*t0 + g*t0**2/2
        v2 += g*t0
        if y >= 0:
            t.goto(x, y)
        else:
            t.goto(x, 0)
    v1 = 0.8 * v1
    v2 = abs(0.8 * v2)
    y = 0
    j += 1
t.exitonclick()
