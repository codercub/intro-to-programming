# guessing_game_letter.py

# Written by @zmagsar
# Jan 12, 2021

import random

alphabet = [chr(dec) for dec in range(97, 123)]
vowels = ["a", "e", "i", "o", "u", "y"]
consonants = [letter for letter in alphabet if letter not in vowels]

letter = random.choice(alphabet)

print("Guess the letter!")
if letter in vowels:
    print("Hint: it's a vowel.")
elif letter in consonants:
    print("Hint: it's a consonant.")

guess = input("Enter a letter: ")
attempt = 1

while letter != guess:
    if letter > guess:
        print("It's after", guess)
    else:
        print("It's before", guess)
        
    guess = input("Enter a letter: ")
    attempt += 1
    if attempt == 4:
        print("Game over.")
        break

else:
    print("You guessed it right,", letter, "is the letter!")
    print("Total attempt:", attempt)