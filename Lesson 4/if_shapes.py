# if_shapes.py

# Written by @zmagsar
# Dec 18, 2020

import turtle as t

t.speed(0)

# Yamar dursiig yamar ongo, hemjeegeer zurahaa oruulah
shape = t.textinput("Shape", "Enter shape:")
color = t.textinput("Color", "Enter color:")
size = int(t.numinput("Size", "Enter size:"))
    
t.begin_fill()
t.color(color, color)

# Hervee dorvoljin gej oruulsan bol dorvoljin zurah
if shape == "square":
    for x in range(4):
        t.forward(size)
        t.left(90)
# Hervee gurvaljin gej oruulsan bol gurvaljin zurah
elif shape == "triangle":
    for x in range(3):
        t.forward(size)
        t.left(120)
# Hervee dugui gej oruulsan bol dugui zurah
elif shape == "circle":
    t.circle(size)
# Deerh 3-iin ali n ch bish bol...
else:
    t.write("Invalid shape!", font = ("Arial", 20, "normal"))
        
t.end_fill()
t.hideturtle()