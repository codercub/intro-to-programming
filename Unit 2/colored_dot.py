# colored_dot.py

# Written by @zmagsar
# Dec 27, 2022

import turtle

color = turtle.textinput("Color", "Enter your favorite color:")
size = turtle.numinput("Size", "How big is your circle?")

turtle.pencolor(color)
turtle.dot(size)


