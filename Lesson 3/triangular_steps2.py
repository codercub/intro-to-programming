# triangular_steps2.py

# Written by Zolbayar Magsar
# Nov 26, 2020

import turtle as t

t.pensize(5)
t.colormode(255)
t.left(60)

for x in range(25):
    t.color((0, 0, 0), (255 - x * 10, 0, 255 - x * 10))
    t.begin_fill()
    for y in range(3):
        t.forward(100 + x * 10)
        t.left(120)
    t.end_fill()
    t.left(30)