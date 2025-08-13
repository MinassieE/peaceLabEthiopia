# Program to list all odd numbers up to a user-specified number

# Get user input
user_input = int(input("Enter a number: "))

print(f"Odd numbers from 0 to {user_input}:")

# Loop through numbers from 0 to user_input
for num in range(user_input + 1):
    if num % 2 != 0:  # Check if number is odd
        print(num, end=" ")