# Example 1: Counting Vowels in a String
word = "programming"
vowel_count = 0

for char in word:
    if char in "aeiouAEIOU":
        vowel_count += 1
        
print(f"The number of vowels in '{word}' is {vowel_count}.")

# Example 2: Password Checker
password = "mysecurepassword123!"
special_chars = "!@#$%^&*"
has_special_char = False

for char in password:
    if char in special_chars:
        has_special_char = True
        break

if has_special_char:
    print("Password contains a special character.")
else:
    print("Password does not contain a special character.")

# Example 3: Finding the Maximum Number in a List
numbers = [3, 5, 2, 8, 1]   
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(f"The maximum number in the list is {max_number}.")


# Example 4: Counting Even Numbers in a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0

for num in numbers:
    # Check if the number is even
    if num % 2 == 0:
        # If it is, increment the counter
        even_count += 1
print(f"The number of even numbers is: {even_count}")