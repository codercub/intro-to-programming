# triangle.py

# Written by Zolbayar Magsar
# Nov 18, 2020
# Adil talt gurvaljin

import turtle

ted = turtle.Pen()

# Ariin ongiig tohiruulah
turtle.bgcolor("black")

# Uzegnii ongiig tohiruulah
ted.pencolor("blue")

# Uzegnii hemjeeg tohiruulah
ted.pensize(5)

# Gurvaljin 3 taltai uchraas 3 udaa davtana
for x in range(3):
    # Gurvaljnii taliig 200 pixel hemjeetei zurna
    ted.forward(200)
    # Adil talt gurvaljnii dotood ontsog 60 gradus uchir gadaad ergeltiin ontsog 120 baina
    ted.left(120)

# Zurj duusaad uzgiig nuuh
ted.hideturtle()