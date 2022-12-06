# triangular_steps1.py

# Written by @zmagsar
# Nov 26, 2020

import turtle as t

t.pensize(5)
t.colormode(255)
t.left(60)

for x in range(48):
    t.color((0, 0, 0), (255 - x * 5, 0, 0))
    t.begin_fill()
    for x in range(3):
        t.forward(100 + x * 10)
        t.left(120)
    t.end_fill()
    t.left(30)