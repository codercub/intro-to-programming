# captain_america.py

# Written by @zmagsar
# Jul 17, 2019

import turtle as t

def move_pen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_circle(size, color):
    t.begin_fill()
    t.color(color, color)
    t.circle(size)
    t.end_fill()
    
def draw_star(size, color):
    t.color(color, color)
    t.begin_fill()
    for x in range(5):
        t.left(72)
        t.forward(size)
        t.right(144)
        t.forward(size)
    t.end_fill()

def main():
    t.speed(0)
    t.bgcolor("black")
    colors = ["crimson", "white", "crimson", "dark blue"]

    # Circles
    for x in range(4):
        move_pen(0, -150 + 30 * x)
        draw_circle(150 - 30 * x, colors[x])

    # Star
    move_pen(-13, 19)
    draw_star(42, "white")

    t.hideturtle()

main()