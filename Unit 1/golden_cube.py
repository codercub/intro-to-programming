import turtle as t

t.title("Golden Cube")
t.speed(0)
t.pensize(5)
t.color("black", "gold")
t.begin_fill()

t.left(30)

for x in range(3):
    t.forward(200)
    t.backward(200)
    t.left(120)
    
t.forward(200)
t.left(120)

for x in range(6):
    t.forward(200)
    t.left(60)
    
t.end_fill()
    
t.hideturtle()