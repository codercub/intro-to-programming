# bigger_circles4.py

# Written by Zolbayar Magsar
# Nov 23, 2020

import turtle as t

t.speed(0)
t.pensize(20)
t.colormode(255)

for x in range(50):
    t.color((0, 0, 200 - x * 2), (0, 0, 255))
    t.penup()
    t.goto(0, 350 - 15 * x)
    t.right(45)
    t.pendown()
    t.begin_fill()
    t.circle(5 * x)
    t.end_fill()