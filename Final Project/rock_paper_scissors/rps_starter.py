import random

# Step 1: Create a list of possible moves
choices = []  # TODO: Add the possible moves

# Step 2: Initialize the scoreboard
player_score = None  # TODO: Set initial player score
computer_score = None  # TODO: Set initial computer score

# Step 3: Welcome message
print("Welcome to Rock-Paper-Scissors!")
print("Type 'quit' to stop the game.\n")

# Step 4: Main game loop
while True:
    # Step 5: Get player input
    player_choice = None  # HINT: .lower() makes input lowercase

    # Step 6: Check if player wants to quit
    if player_choice == "quit":
        # TODO: Print final score before ending the game
        break

    # Step 7: Validate input
    if player_choice not in choices:
        # TODO: Print invalid choice message
        continue  # Skip this round and go back to the start

    # Step 8: Computer makes a random choice
    computer_choice = random.choice(choices)
    # TODO: Print computer's choice

    # Step 9: Decide the winner
    if player_choice == computer_choice:
        # TODO: Print tie message
        pass
    elif (
        #logic to determine if player wins
    ):
        # TODO: Print win message and update player_score
        pass
    else:
        # TODO: Print lose message and update computer_score
        pass

    # Step 10: Show the updated score
    # TODO: Print scoreboard