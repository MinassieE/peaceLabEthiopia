# Example 1: Checking an Answer in a Quiz
user_answer = input("Give your answer (A, B, C, or D): ")
correct_answer = "B"

if user_answer: # Checks if the variable isn't empty
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect. Try again.")
else:
    print("Please select an answer.")



