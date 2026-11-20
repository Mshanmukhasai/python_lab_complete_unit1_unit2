from datetime import datetime
import math

try:
    entry = input("Enter entry date and time (YYYY-MM-DD HH:MM): ")
    exit_time = input("Enter exit date and time (YYYY-MM-DD HH:MM): ")

    entry_time = datetime.strptime(entry.strip(), "%Y-%m-%d %H:%M")
    exit_datetime = datetime.strptime(exit_time.strip(), "%Y-%m-%d %H:%M")

    if exit_datetime <= entry_time:
        print("Error: Exit time must be later than entry time.")

    else:
        duration = exit_datetime - entry_time
        total_minutes = duration.total_seconds() / 60

        billable_hours = math.ceil(total_minutes / 60)

        fee = 30 + (billable_hours - 1) * 20
        final_fee = min(fee, 250)

        print("\n--- Parking Fee Details ---")
        print("Entry Time:", entry_time)
        print("Exit Time:", exit_datetime)
        print("Parking Duration:", duration)
        print("Billable Hours:", billable_hours)
        print("Fee Before Maximum Limit: ₹", fee)
        print("Final Parking Fee: ₹", final_fee)

except ValueError:
    print("Error: Enter the date and time in the correct format.")