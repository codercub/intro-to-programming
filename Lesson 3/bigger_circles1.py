# bigger_circles1.py

# Written by @zmagsar
# Nov 23, 2020

import turtle as t

for x in range(5):
    t.penup()
    t.goto(0, -x * 25 - 50) # -50 -75 -100 -125 -150
    t.pendown()
    t.circle(x * 25 + 50) # 50 75 100 125 150