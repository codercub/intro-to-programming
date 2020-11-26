# snowflake2.py

# Written by Zolbayar Magsar
# Nov 23, 2020

import turtle as t

t.speed(0)
t.pensize(5)
t.colormode(255)

for x in range(10):
    t.pencolor((0 + 20 * x, 0, 255 - x * 20))
    for y in range(2):
        t.forward(200)
        t.right(60)
        t.forward(200)
        t.right(120)
    t.left(36)