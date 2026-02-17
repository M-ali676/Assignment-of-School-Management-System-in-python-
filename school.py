# 4. Student Grade Management System (M,N,O,P)
# Ask the user for the number of students.


# For each student, input marks (must be between 0–100).
# Assign grades (A, B, C, Fail).
# If marks > 85, show “Distinction”.
# Outer for → students
# Inner while → validate marks
# if-elif-else → grade assignment
# Nested if → distinction check


print("****** Student Grading System ************")

students = int(input("Enter the number of students: "))
student_count=1
while student_count <= 5:
    while True:
        marks = int(input(f"Enter marks for student {student_count} (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")
    if marks > 85:
        grade = "A1+"
        remarks = "Excellent"
    elif marks > 70:
        grade = "B"
        remarks = "Good"
    elif marks > 50:
        grade = "C"
        remarks = "Average"
    else:
        grade = "Fail"
        remarks = "Failed"
    print(f"\n1.Student {student_count}: \n2.Marks = {marks},\n3. Grade = {grade}, \n4.Remarks = {remarks}")
    student_count += 1
for i in range(students):
    while True:
        marks = int(input(f"Enter marks for students {i + 1} (0-100): "))
        if 0 <= marks <=100:
            break
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")
    if marks > 90:
        grade = "A1+"
        remarks = "Excellent"
    elif marks > 80:
        grade = "A"
        remarks = "Good"
    elif marks > 70:
        grade = "B+"
        remarks = "Average"
    elif marks > 60:
        grade = "B"
        remarks = "Below Average"
    elif marks > 50:
        grade = "C+"
        remarks = "Poor"
    elif marks > 40:
        grade = "C"
        remarks = "Failed"
    else:
        grade = "Fail"
        remarks = "Failed"
        print(f"Student {i + 1}: Marks = {marks}, Grade = {grade}, Remarks = {remarks}")
