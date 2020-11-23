# microsoft_logo.py

# Written by Zolbayar Magsar
# Nov 17, 2020
# Function ashiglaagui huvilbar

import turtle as t

t.speed(0)

# Ulaan dorvoljin
t.penup()
t.goto(-450, 5)
t.pendown()
t.color("orange red", "orange red")
t.begin_fill()
for x in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
        
# Tsenkher dorvoljin
t.penup()
t.goto(-450, -105)
t.pendown()
t.color("deep sky blue", "deep sky blue")
t.begin_fill()
for x in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# Nogoon dorvoljin
t.penup()
t.goto(-340, 5)
t.pendown()
t.color("yellow green", "yellow green")
t.begin_fill()
for x in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# Shar dorvoljin
t.penup()
t.goto(-340, -105)
t.pendown()
t.color("gold", "gold")
t.begin_fill()
for x in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# Microsoft bichig
t.penup()
t.goto(-200, -100)
t.pendown()
t.pencolor("grey")
t.write("Microsoft", font = ("Segoe UI", 80, "normal"))
    
t.hideturtle()