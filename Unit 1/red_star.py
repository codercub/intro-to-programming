# red_star.py

# Written by @zmagsar
# Nov 25, 2020
# Olon ontsogtuud

import turtle as t

t.speed(0)

t.color("red")

t.begin_fill()

for x in range(5):
    t.forward(100)
    t.left(72)
    t.forward(100)
    t.right(144)
    
t.end_fill()

t.hideturtle()