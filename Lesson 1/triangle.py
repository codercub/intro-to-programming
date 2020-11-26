# triangle.py

# Written by Zolbayar Magsar
# Nov 18, 2020
# Adil talt gurvaljin

import turtle

# Ariin ongiig tohiruulah
turtle.bgcolor("black")

# Uzegnii ongiig tohiruulah
turtle.pencolor("blue")

# Uzegnii hemjeeg tohiruulah
turtle.pensize(5)

# Gurvaljin 3 taltai uchraas 3 udaa davtana
for x in range(3):
    # Gurvaljnii taliig 200 pixel hemjeetei zurna
    turtle.forward(200)
    # Adil talt gurvaljnii gadaad ontsog 120
    turtle.left(120)

# Zurj duusaad uzgiig nuuh
turtle.hideturtle()