# star_polygon.py

# Written by Zolbayar Magsar
# Nov 25, 2020
# Olon ontsogtuud

# https://en.wikipedia.org/wiki/Regular_polygon

import turtle

ted = turtle.Pen()

# Daraah ajluudiig hiih:
# 1. Davtaltiin too bolon ergeltiin gradusiin hoorondiin hamaarliig ajiglah, uund:
# - 5 hoshuunii huvid niit radius: 180 x 3 = 720
# - Tiimees tavan hoshuunii huvid 5 x 144 = 720 baina
# 2. Davtaltiin too bolon ergeltiin gradusiig oorchilj octagram durs zurah, uund:
# - 8 hoshuunii huvid niit radius 180 x 6 = 1080

for x in range(5):
    ted.forward(300)
    ted.right(144)

ted.hideturtle()