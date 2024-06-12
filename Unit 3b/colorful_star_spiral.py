# colorful_star_spiral.py

# Written by @zmagsar
# Dec 5, 2020

import turtle as t

t.pensize(5)
COLORS = ["red", "pink", "brown", "orange", "purple"]

for x in range(100):
    t.pencolor(COLORS[x % 5])
    t.forward(x * 10)
    t.right(144)