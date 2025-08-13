# Activity 1: Write a code that checks a variable ‘score’ and grade the score.
# If score is greater than or equal to 90, print "A"
# If score is greater than or equal to 80 but less than 90, print "B"
# If score is greater than or equal to 70 but less than 80, print "C"
# If score is greater than or equal to 60 but less than 70, print "D"
# If score is less than 60, print "F"

score = 85
# score = float(input("Enter the score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")