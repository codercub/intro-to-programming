# chrome.py

# Written by @zmagsar
# May 4, 2022

import turtle as t

t.speed(0)
t.pensize(4)

COLORS = ['forest green', 'gold', 'red']

t.dot(44, 'dodger blue')
t.penup()
t.goto(0, -55)
t.pendown()
t.left(60)

for x in range(40):
    for y in range(3):
        t.color(COLORS[y % 3])
        t.forward(95)
        t.left(119)

t.hideturtle()

t.penup()
t.goto(-50, -150)
t.pendown()
t.pencolor("grey")
t.write("CHROME", font = ("Segoe", 40, "normal"))