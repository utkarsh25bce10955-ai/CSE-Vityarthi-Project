# CGPA Calculator

# Grade to grade-point mapping
grade_points = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5,
    "F": 0
}

print("=== CGPA Calculator ===")

# Number of subjects
n = int(input("Enter number of subjects: "))

total_points = 0
total_credits = 0

for i in range(n):
    print(f"\nSubject {i+1}:")
    
    # Get valid credit input
    while True:
        credit = int(input("Enter credits (1, 2, 3, or 4): "))
        if credit in [1, 2, 3, 4]:
            break
        else:
            print("Invalid credit. Please enter 1, 2, 3, or 4.")
    
    # Get valid grade input
    while True:
        grade = input("Enter grade (S/A/B/C/D/E/F): ").upper()
        if grade in grade_points:
            break
        else:
            print("Invalid grade. Enter one of S A B C D E F.")
    
    # Calculate weighted score
    points = grade_points[grade]
    total_points += points * credit
    total_credits += credit

# Compute CGPA
cgpa = total_points / total_credits

print("\n------------------------")
print(f"Your CGPA is: {cgpa:.2f}")
print("------------------------")