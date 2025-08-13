def grade_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example 1: fixed value
score = 85
print("Grade:", grade_score(score))

# Example 2: user input
score = float(input("Enter your score: "))
print("Grade:", grade_score(score))