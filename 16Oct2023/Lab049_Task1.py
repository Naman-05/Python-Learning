#Write a program that calculates and displays the letter grade for a given
#numerical score (e.g., A, B, C, D, or F) based on the following grading scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("Enter your Marks obtained: "))
if score <= 100 and score >= 90:
    print("Your Grade is A")
elif score <= 89 and score >= 80:
    print("Your Grade is B")
elif score <= 79 and score >= 70:
    print("Your Grade is C")
elif score <= 69 and score >= 60:
    print("Your Grade is D")
elif score <= 59:
    print("Your Grade is F")
else:
    print("Invalid input")