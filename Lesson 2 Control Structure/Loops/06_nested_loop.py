# Example 1: All Possible Pairs of Letters
letters = ["A", "B", "C"]

for first in letters:
    for second in letters:
        print(first, second)


# Example 2: Multiplication Table
# This code generates a multiplication table from 1 to 3.
for i in range(1, 4):      # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"{i} x {j} = {i*j}")


# Example 3: Nested Loop to Print a Square Pattern
# This code prints a 3x3 square of asterisks.
for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()