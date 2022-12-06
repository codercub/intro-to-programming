# convex_polygon.py

# Written by @zmagsar
# Nov 18, 2020
# Olon ontsogtuud

import turtle

# Hurdan zurah
turtle.speed(0)

# Daraah ajluudiig hiih:
# 1. Davtaltiin too bolon ergeltiin gradusiin hoorondiin hamaarliig ajiglah, uund:
# - Niit radius: 180 x 2 = 360
# - Dorvoljin 4 * 90 = 360, gurvaljin 3 * 120 = 360, pentagon 5 * 72 = 360 geh met...
# 2. 6, 8, 10 talt dursuud zurah
# 3. Davtaltiig ihesgej, ergeltiin ontsog bolon taluudiig bagasgasnaar toirog zurah
for x in range(5):
    turtle.forward(100)
    turtle.left(72)

turtle.hideturtle()