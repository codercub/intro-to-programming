# captain_america.py

# Written by @zmagsar
# Feb 18, 2024

import turtle as t

# Circles
t.dot(500, "crimson")
t.dot(400, "white")
t.dot(300, "crimson")
t.dot(200, "dark blue")

# Move pen
t.goto(21, 32)

# Star
t.color("white")
t.begin_fill()
for x in range(5):
    t.forward(72)
    t.right(144)
    t.forward(72)
    t.left(72)
t.end_fill()