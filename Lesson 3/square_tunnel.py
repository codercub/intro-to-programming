# square_tunnel.py

# Written by Zolbayar Magsar
# Jul 20, 2020

import turtle as t

t.speed(0)
t.colormode(255)
t.bgcolor(0, 0, 0)
t.pensize(20)

for x in range(25):
    t.pencolor(0, 255 - x * 10, 255 - x * 10)
    t.penup()
    t.goto(-400 + x * 10, -380 + x * 10)
    t.pendown()
    for y in range(4):
        t.forward(20 * x + 100)
        t.left(90)

t.hideturtle()