# colorful_square_spiral.py

# Written by @zmagsar
# Dec 5, 2020

import turtle as t

COLORS = ["red", "green", "blue", "yellow"]

for x in range(100):
    t.pencolor(COLORS[x % 4])
    t.forward(x)
    t.left(90)