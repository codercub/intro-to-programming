# sun_function.py

# Written by @zmagsar
# Nov 23, 2020

import turtle as t

def move_pen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def sun_ray(x, y, size):
    move_pen(x, y)
    t.forward(size)
    t.left(45)

def main():
    t.speed(0)
    t.bgcolor("sky blue")
    t.color("gold", "gold")
    t.pensize(5)
    x_coor = [110, 80, 0, -80, -110, -80, 0, 80]
    y_coor = [0, 80, 110, 80, 0, -80, -110, -80]

    # sun
    t.dot(200)

    # sun ray
    for i in range(8):
        sun_ray(x_coor[i], y_coor[i], 200)

    t.hideturtle()

main()