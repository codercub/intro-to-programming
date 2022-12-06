# star_polygon.py

# Written by @zmagsar
# Nov 25, 2020
# Olon ontsogtuud

import turtle

# Daraah ajluudiig hiih:
# 1. Davtaltiin too bolon ergeltiin gradusiin hoorondiin hamaarliig ajiglah, uund:
# - 5 hoshuunii huvid niit radius: 180 x 3 = 720
# - Tiimees tavan hoshuunii huvid 5 x 144 = 720 baina
# 2. Davtaltiin too bolon ergeltiin gradusiig oorchilj octagram durs zurah, uund:
# - 8 hoshuunii huvid niit radius 180 x 6 = 1080

for x in range(5):
    turtle.forward(300)
    turtle.right(144)

turtle.hideturtle()