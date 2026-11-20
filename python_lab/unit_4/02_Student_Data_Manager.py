STUDENT_FILE = "students.txt"


while True:
    print("\n----- STUDENT DATA MANAGER -----")
    print("1. Add a new student record")
    print("2. Display all student records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ").strip()
        name = input("Enter Student Name: ").strip()
        marks = input("Enter Marks: ").strip()

        if not roll_no or not name or not marks:
            print("Roll number, name, and marks cannot be empty.")
            continue

        with open(STUDENT_FILE, "a", encoding="utf-8") as file:
            file.write(f"{roll_no},{name},{marks}\n")
        print("Student record added successfully!")

    elif choice == "2":
        try:
            with open(STUDENT_FILE, "r", encoding="utf-8") as file:
                records = file.readlines()

            if not records:
                print("No student records found.")
            else:
                print("\n----- STUDENT RECORDS -----")
                for record in records:
                    fields = record.strip().split(",", 2)
                    if len(fields) != 3:
                        continue

                    roll_no, name, marks = fields
                    print("Roll Number:", roll_no)
                    print("Student Name:", name)
                    print("Marks:", marks)
                    print("--------------------------")
        except FileNotFoundError:
            print("No student records found. File does not exist.")

    elif choice == "3":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please try again.")
