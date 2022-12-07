# microsoft_logo.py

# Written by @zmagsar
# Nov 17, 2020
# Function ashiglaagui huvilbar

import turtle as t

t.speed(0)

# Ulaan dorvoljin
t.penup()
t.goto(-250, 0)
t.pendown()
t.color("orange red", "orange red")
t.begin_fill()
for x in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()
        
# Tsenkher dorvoljin
t.penup()
t.goto(-250, -55)
t.pendown()
t.color("deep sky blue", "deep sky blue")
t.begin_fill()
for x in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

# Nogoon dorvoljin
t.penup()
t.goto(-195, 0)
t.pendown()
t.color("yellow green", "yellow green")
t.begin_fill()
for x in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

# Shar dorvoljin
t.penup()
t.goto(-195, -55)
t.pendown()
t.color("gold", "gold")
t.begin_fill()
for x in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

# Microsoft bichig
t.penup()
t.goto(-120, -50)
t.pendown()
t.pencolor("grey")
t.write("Microsoft", font = ("Segoe", 80, "normal"))
    
t.hideturtle()