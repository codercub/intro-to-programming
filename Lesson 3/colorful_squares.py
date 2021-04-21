# colorful_squares.py

# Written by @zmagsar
# April 21, 2021

import turtle as t

COLORS = ["cornflower blue", "silver", "indigo", "coral", "dark blue", "chartreuse"]

t.speed(0)
t.pensize(4)
side = 100
jump = 50
times = 6

for x in range(times):
    t.color(COLORS[x])
    for y in range(4):
        t.forward(side)
        t.left(90)
    t.forward(jump)
    t.right(60)
    
t.hideturtle()