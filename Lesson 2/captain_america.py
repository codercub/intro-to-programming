# captain_america.py

# Written by @zmagsar
# Jul 17, 2019

import turtle as t

t.speed(0)
t.bgcolor("black")
colors = ["crimson", "white", "crimson", "dark blue"]

# Circles
for x in range(4):
    t.dot(300 - 60 * x, colors[x])

# Star
t.penup()
t.goto(-13, 19)
t.pendown()
t.color("white", "white")
t.begin_fill()
for x in range(5):
    t.left(72)
    t.forward(42)
    t.right(144)
    t.forward(42)
t.end_fill()

t.hideturtle()