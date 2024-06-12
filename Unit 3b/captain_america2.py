# captain_america2.py

# Written by @zmagsar
# Jul 17, 2019

import turtle as t

t.title("Captain America's Shield")
t.speed(0)
t.bgcolor("black")
COLORS = ["crimson", "white", "crimson", "dark blue"]

# Booronhiinuudiig zurah
for x in range(4):
    t.dot(300 - 60 * x, COLORS[x])

# (-14, 19) tseg ruu ochih
t.goto(-14, 19)

# Star zurah
t.color("white", "white")
t.begin_fill()
for x in range(5):
    t.left(72)
    t.forward(43)
    t.right(144)
    t.forward(43)
t.end_fill()

t.hideturtle()