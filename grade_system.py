# grading system

subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))


total_marks = subject1 + subject2 + subject3 + subject4 + subject5


percentage = (total_marks / 500) * 100


print(f"Percentage: {percentage:.2f}%")


if percentage >= 85:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 65:
    grade = "C"
else:
    grade = "D"


print(f"Grade: {grade}")
