import csv

PAYROLL_FILE = "payroll.csv"
FIELDNAMES = ["employee_id", "name", "hours_worked", "hourly_rate", "gross_pay"]


def load_payroll():
    try:
        with open(PAYROLL_FILE, "r", newline="", encoding="utf-8") as payroll_file:
            reader = csv.DictReader(payroll_file)
            if reader.fieldnames != FIELDNAMES:
                raise ValueError(
                    f"{PAYROLL_FILE} must have these columns: {', '.join(FIELDNAMES)}"
                )
            return list(reader)
    except FileNotFoundError:
        return []


def save_payroll(records):
    with open(PAYROLL_FILE, "w", newline="", encoding="utf-8") as payroll_file:
        writer = csv.DictWriter(payroll_file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(records)


while True:
    print("\n--- PAYROLL MANAGEMENT ---")
    print("1. Add Payroll Record")
    print("2. View Payroll Records")
    print("3. Exit")

    choice = input("Enter your choice: ")
    records = load_payroll()

    if choice == "1":
        employee_id = input("Enter employee ID: ").strip()
        if any(record["employee_id"] == employee_id for record in records):
            print("A payroll record with that ID already exists.")
            continue

        name = input("Enter employee name: ").strip()
        try:
            hours_worked = float(input("Enter hours worked: "))
            hourly_rate = float(input("Enter hourly rate: "))
        except ValueError:
            print("Hours worked and hourly rate must be numbers.")
            continue

        if hours_worked < 0 or hourly_rate < 0:
            print("Hours worked and hourly rate cannot be negative.")
            continue

        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)
        gross_pay = regular_hours * hourly_rate + overtime_hours * hourly_rate * 1.5

        records.append(
            {
                "employee_id": employee_id,
                "name": name,
                "hours_worked": f"{hours_worked:.2f}",
                "hourly_rate": f"{hourly_rate:.2f}",
                "gross_pay": f"{gross_pay:.2f}",
            }
        )
        save_payroll(records)
        print(f"Payroll record added. Gross pay: ${gross_pay:.2f}")

    elif choice == "2":
        if len(records) == 0:
            print("No payroll records available.")
        else:
            print("\n--- PAYROLL RECORDS ---")
            for record in records:
                print(
                    f"ID: {record['employee_id']}, Name: {record['name']}, "
                    f"Hours: {record['hours_worked']}, "
                    f"Rate: ${record['hourly_rate']}, "
                    f"Gross Pay: ${record['gross_pay']}"
                )

    elif choice == "3":
        print("Exiting Payroll Management...")
        break

    else:
        print("Invalid choice.")
