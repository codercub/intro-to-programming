import turtle as t

t.speed(0)
t.bgcolor("red")
t.pencolor("white")
t.pensize(25)

for x in range(360):
    t.forward(1)
    t.left(1)

for x in range(360):
    t.forward(1.2)
    t.right(1)
    
t.hideturtle()