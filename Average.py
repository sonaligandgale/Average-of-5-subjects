# Student Grade Evaluation Program

# Input marks of 5 subjects
marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

# Calculate average
average = sum(marks) / 5

# Determine Grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

# Output
print("\n----- RESULT -----")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
