#Example 1
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend! Time to relax.")
else:
    print("It's a weekday.")

# Example 2
is_girl = True
is_student = True

if is_girl and is_student:
    print("You can take this training.")
else:
    print("You do not meet the requirements for this training.")

# Example 3
is_raining = False

if not is_raining:
    print("It's not raining, so you can go outside!")
else:
    print("It is raining, so you should bring an umbrella.")

# Example 4
age = int(input("Enter your age: "))
average_grade = float(input("Enter your average grade: "))

if age < 20 and average_grade >= 90:
    print("Congratulations! You are eligible for a scholarship.")
else:
    print("Sorry, you do not meet the scholarship requirements.")
