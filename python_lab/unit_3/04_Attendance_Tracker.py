attendance = {}

while True:
    print("\n--- ATTENDANCE TRACKER ---")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. View Attendance Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip()
        if not name:
            print("Student name cannot be empty.")
            continue

        status = input("Enter status (Present/Absent): ").strip().lower()
        if status == "present":
            attendance[name] = "Present"
        elif status == "absent":
            attendance[name] = "Absent"
        else:
            print("Invalid status. Enter Present or Absent.")
            continue

        print("Attendance recorded successfully.")

    elif choice == "2":
        if len(attendance) == 0:
            print("No attendance records available.")
        else:
            print("\n--- ATTENDANCE RECORDS ---")
            for name, status in attendance.items():
                print(f"{name}: {status}")

    elif choice == "3":
        present_count = sum(status == "Present" for status in attendance.values())
        absent_count = sum(status == "Absent" for status in attendance.values())
        print("Total students:", len(attendance))
        print("Present:", present_count)
        print("Absent:", absent_count)

    elif choice == "4":
        print("Exiting Attendance Tracker...")
        break

    else:
        print("Invalid choice.")
