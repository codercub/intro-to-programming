# octagram_steps.py

# Written by Zolbayar Magsar
# Nov 23, 2020

import turtle as t

t.speed(0)
t.colormode(255)

for x in range(100):
    t.penup()
    t.goto(-200 + x * 5, -200 + x * 5)
    t.pendown()
    # square
    t.color(0, 0, 50 + x * 2)
    t.right(45)
    t.begin_fill()
    for y in range(4):
        t.forward(50 + x * 2)
        t.left(90)
    t.end_fill()