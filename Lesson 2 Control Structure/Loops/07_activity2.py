# Instructions:
# Task: Build a Number Guessing Game
# The program should pick a secret number between 1 and 10.
# The player has 3 attempts to guess it.
# After each guess:
# If correct → print “🎉 You guessed it!” and stop the game.
# If wrong → tell them if the secret number is higher or lower.
# If the player uses all 3 attempts without guessing → print “❌ Game over! The number was X.”
# 💡 Hint: Use random.randint(1, 10) to choose the secret number and a while loop to count attempts.

import random

secret = random.randint(1, 10)
attempts = 3

print("Guess the number (1–10). You have 3 tries.")

while attempts > 0:
    guess = int(input("Your guess: "))
    if guess == secret:
        print("🎉 Correct!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    attempts -= 1

if guess != secret:
    print(f"❌ Game over! The number was {secret}.")