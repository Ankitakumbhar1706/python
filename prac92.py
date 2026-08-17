print("===== STUDENT SCORE FILTER =====")

grades = []

n = int(input("Enter number of students: "))

for i in range(n):
    grade = int(input(f"Enter grade {i + 1}: "))
    grades.append(grade)
    print("\n========***=======")

print("\nOriginal grades:", grades)



index = int(input("Enter index position to update: "))


new_grade = int(input("Enter new grade: "))

grades[index] = new_grade


print("\nCorrected grades:", grades)