import sys

if len(sys.argv) == 6:
    script_name = sys.argv[0]
    m1 = float(sys.argv[1])
    m2 = float(sys.argv[2])
    m3 = float(sys.argv[3])
    m4 = float(sys.argv[4])
    m5 = float(sys.argv[5])
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    m1 = 80.0
    m2 = 75.0
    m3 = 90.0
    m4 = 85.0
    m5 = 70.0
    print("No input given – using default marks:")

average = (m1 + m2 + m3 + m4 + m5) / 5

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "Fail"

print("Script Name:", script_name)
print("Marks:", m1, m2, m3, m4, m5)
print("Average marks:", average)
print("Grade:", grade)
