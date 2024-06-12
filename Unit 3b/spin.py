# spin.py

# Written by @zmagsar
# May 8, 2021

import turtle as t

length = 10

t.penup()
t.goto(0, 250)
t.pendown()
t.pensize(5)
t.bgcolor("black")
t.pencolor("dark turquoise")
t.right(90)

for x in range(12):
    t.forward(10)
    t.right(90)
    t.forward(length)
    length += 10
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(length)
    length += 10
    t.right(90)
    
for x in range(13):
    t.forward(10)
    t.right(90)
    t.forward(length)
    length -= 10
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(length)
    length -= 10
    t.right(90)
    
t.hideturtle()