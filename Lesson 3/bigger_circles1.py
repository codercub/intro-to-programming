# bigger_circles1.py

# Written by Zolbayar Magsar
# Nov 23, 2020

import turtle as t

for x in range(5):
    t.penup()
    t.setpos(0, -x * 25 - 50)
    t.pendown()
    t.circle(x * 25 + 50)