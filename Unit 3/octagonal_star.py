# octagonal_star.py

# Written by @zmagsar
# Dec 2, 2020

import turtle as t

t.title("Octagonal Star With Rainbow Colors")
t.pensize(3)
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "white"]

for x in range(8):
    t.color("black", COLORS[x])
    t.begin_fill()
    for y in range(2):
        t.forward(100)
        t.right(45)
        t.forward(100)
        t.right(135)
    t.end_fill()
    t.right(45)

t.hideturtle()