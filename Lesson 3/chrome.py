import turtle as t

t.speed(0)
t.pensize(4)

COLORS = ['red', 'forest green', 'gold']

t.color('dodger blue')

t.dot(46)
t.penup()
t.goto(-50, -29)
t.pendown()

for x in range(61):
    for y in range(3):
        t.color(COLORS[y % 3])
        t.forward(100)
        t.left(119)
        
t.hideturtle()