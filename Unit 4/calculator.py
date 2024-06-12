# calculator.py

# Written by @zmagsar
# Dec 12, 2020

# Ehnii toogoo oruulah
n1 = int(input("Enter number 1: "))

# Daraagiin toogoo oruulah
n2 = int(input("Enter number 2: "))

# Uildel oruulah
operator = input("Enter the operator (+ - * /): ")

# Uildlees hamaarch "result" huvisagchid ur dung bodoj hadgalah
if operator == "+":
    result = n1 + n2
elif operator == "-":
    result = n1 - n2
elif operator == "*":
    result = n1 * n2
elif operator == "/":
    result = n1 / n2
else:
    result = "ERROR :("

# Hariug hevleh
print("The result is:", result)