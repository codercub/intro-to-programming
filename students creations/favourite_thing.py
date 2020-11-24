# favourite_thing.py
# Written by Tuguldur Jaminsuren

import turtle as b
b.speed(0)
b.penup()
b.setpos(-70, 0)
b.pendown()

b.bgcolor("brown")
b.pensize(4)

#Book size and shape
b.right(45)
b.color("black", "green")
b.begin_fill()

for x in range(2):
         b.forward(100)
         b.left(90)
         b.forward(170)
         b.left(90)

b.end_fill()

#Book heigt
b.right(45)
b.begin_fill()

b.color("black", "orange")
b.forward(30)
b.left(45)
b.forward(100)
b.left(90)
b.forward(170)
b.left(45)
b.forward(30)
b.left(135)
b.forward(170)
b.right(90)
b.forward(100)

b.end_fill()

b.backward(100)
b.left(135)
b.forward(30)

#Book sign
b.penup()
b.setpos(30, 72.6)
b.pendown()

b.left(45)
b.begin_fill()
b.color("black", "white")
for x in range(2):
    b.forward(60)
    b.left(90)
    b.forward(30)
    b.left(90)

b.end_fill()

#Word
b.penup()
b.setpos(40, 72.6)
b.pendown()

b.forward(45)

#Bottom word
b.penup()
b.setpos(-20, 20)
b.pendown()
b.forward(60)
b.penup()
b.setpos(-30, 10)
b.pendown()
b.forward(60)
b.penup()
b.setpos(-40, 0)
b.pendown()
b.forward(60)
b.hideturtle()
