# bmi_calc.py

# Written by @zmagsar
# Nov 29, 2020

# Body Mass Index oloh program

# INPUT
w = int(input("Jin (kg): "))
h = float(input("Ondor (m): "))

# PROCESSING
bmi = w / h ** 2 

# OUTPUT
print("Tanii BMI:", round(bmi))