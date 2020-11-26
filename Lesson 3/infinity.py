# infinity.py

# Written by Zolbayar Magsar
# Nov 23, 2020

import turtle as t

t.speed(0)
t.colormode(255)
t.bgcolor(255, 100, 0)
t.pensize(25)

t.right(90)

for x in range(10):
    t.pencolor(0, 0, 255 - x * 20)
    for y in range(360):
        t.forward(1 + x * 0.2)
        t.left(1)

    for y in range(360):
        t.forward(1 + x * 0.2)
        t.right(1)
    
t.hideturtle()