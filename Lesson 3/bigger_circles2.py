# bigger_circles2.py

# Written by @zmagsar
# Nov 23, 2020

import turtle as t

t.speed(0)
t.color("red")

for x in range(100):
    t.penup()
    t.setpos(-300 + x * 10, -300 + x * 10)
    t.pendown()
    t.left(1)
    t.circle(50 + x * 10)
    
t.hideturtle()