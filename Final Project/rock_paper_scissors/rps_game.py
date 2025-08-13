import random

# Possible moves
choices = ["rock", "paper", "scissors"]

# Scoreboard
player_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors!")
print("Type 'quit' to stop the game.\n")

while True:
    # Player input
    player_choice = input("Enter rock, paper, or scissors: ").lower()

    if player_choice == "quit":
        print("\nFinal Score:")
        print(f"You: {player_score} | Computer: {computer_score}")
        break

    if player_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Decide winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score}\n")