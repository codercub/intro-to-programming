# rectangle.py

# Written by @zmagsar
# Nov 29, 2020

# Ogogdson hemjees, ongonii daguu tegsh ontsogt zurah

import turtle as t

t.speed(0)

# Hemjeesuud bolon ongiig oruulah
urt = int(t.numinput("Breadth", "Tegsh ontsogtiin urt: "))
orgon = int(t.numinput("Width", "Tegsh ontsogtiin orgon: "))
ongo = t.textinput("Color", "Ongo: ")

# Ogogdson ongoor uzegnii ongiig taaruulah
t.color(ongo, ongo)

t.begin_fill()

# Ogogdson hemjeesuudeer zurah
for x in range(2):
    t.forward(urt)
    t.left(90)
    t.forward(orgon)
    t.left(90)
    
t.end_fill()

t.hideturtle()