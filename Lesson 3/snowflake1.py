# snowflake1.py

# Written by @zmagsar
# Nov 23, 2020

import turtle as t

t.speed(0)
t.bgcolor("dark blue")
t.color("cyan")
t.pensize(2)

for x in range(12):
    for y in range(2):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
    t.right(30)
    
t.hideturtle()