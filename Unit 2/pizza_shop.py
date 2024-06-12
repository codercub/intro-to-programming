# pizza_shop.py

# Written by @zmagsar
# Nov 29, 2020

# Pizzanii restoranii kassnii program

# INPUT
pizza_une = int(input("Pizzanii une: "))
pizza_shirheg = int(input("Heden pizza: "))
undaa_une = int(input("Undaanii une: "))
undaa_shirheg = int(input("Heden undaa: "))

# PROCESSING
tatvargui_une = pizza_une * pizza_shirheg + undaa_une * undaa_shirheg
tatvar = tatvargui_une * 0.1
niit = tatvargui_une + tatvar

# OUTPUT
print("Tanii toloh dun:", niit)