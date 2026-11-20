student_name = input("Enter student name: ")
subject_count = int(input("Enter number of subjects: "))

if subject_count <= 0:
    print("Number of subjects must be at least 1.")
else:
    marks = {}

    for subject_number in range(1, subject_count + 1):
        subject = f"Subject {subject_number}"
        marks[subject] = float(input(f"Enter marks for {subject} (0-100): "))

    total = sum(marks.values())
    average = total / subject_count

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print("\n--- STUDENT GRADE REPORT ---")
    print("Name:", student_name)
    for subject, mark in marks.items():
        print(f"{subject}: {mark}")
    print("Total Marks:", total)
    print(f"Average: {average:.2f}")
    print("Grade:", grade)
