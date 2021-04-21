# colorful_star.py

# Written by @zmagsar
# April 7, 2021

import turtle as t

t.speed(0)
t.pensize(20)

COLORS = ["magenta", "purple", "navy", "crimson", "cyan"]

for x in range(5):
    t.color(COLORS[x])
    t.forward(200)
    t.right(144)

t.hideturtle()