# guessing_game_number.py

# Written by @zmagsar
# Jan 12, 2021

import random

# 1~10 toonuudaas duriin too songoh
number = random.randint(1, 10)

# Ehnii udaa taah
guess = int(input("Enter number 1~10: "))
attempt = 1

# Hervee buruu taasan bol dahij 2 udaa taah bolomj
while guess != number:
    if guess > number:
        print("Go lower!")
    else:
        print("Go higher!")
    guess = int(input("Enter number 1~10: "))
    attempt += 1
    if attempt == 4:
        print("Game over.")
        break

# Toog zov taasan tohioldold
else:
    print("You guessed it right,", number, "is the number!")
    print("Number of attempts:", attempt)