# house.py

# Written by @zmagsar
# Mar 18, 2023
# Baishin zurah

import turtle as t

t.speed(0)
t.bgcolor("sky blue")

t.penup()
t.goto(-500, -200)
t.pendown()

# land
t.color("green")
t.begin_fill()
for x in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

t.forward(800)

# building
t.color("saddle brown")

t.begin_fill()
for x in range(4):
    t.left(90)
    t.forward(400)
t.end_fill()

t.backward(50)

# door
t.color("yellow")
t.begin_fill()
for x in range(2):
    t.left(90)
    t.forward(250)
    t.left(90)
    t.forward(100)
t.end_fill()

t.penup()
t.home()

# window
t.color("light blue")

for x in range(4):
    t.begin_fill()
    for y in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()
    t.right(90)
    t.forward(10)

t.penup()
t.goto(-120, 200)
t.pendown()

# roof
t.color("red")
t.begin_fill()
t.forward(440)
t.left(150)
t.forward(254)
t.left(60)
t.forward(254)
t.end_fill()

t.hideturtle()
