# bigger_circles3.py

# Written by @zmagsar
# Nov 23, 2020

import turtle as t

t.speed(0)
t.pensize(20)
t.colormode(255)

for x in range(50):
    t.pencolor(255 - x * 5, 100 - x * 2, 0)
    t.penup()
    t.goto(0, 380 - 15 * x)
    t.pendown()
    t.circle(5 * x)