import json


LOG_FILE = "logs.json"


try:
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Invalid JSON data: Expected a list of logs.")

    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    print("\n----- ALL LOG RECORDS -----")
    for log in data:
        if not isinstance(log, dict):
            print("Invalid log record:", log)
            continue

        timestamp = log.get("timestamp", "N/A")
        level = str(log.get("level", "N/A")).upper()
        message = log.get("message", "N/A")

        print("Timestamp:", timestamp)
        print("Level:", level)
        print("Message:", message)
        print("--------------------------")

        if level in counts:
            counts[level] += 1

    print("\n----- LOG SUMMARY -----")
    print("Total INFO messages:", counts["INFO"])
    print("Total WARNING messages:", counts["WARNING"])
    print("Total ERROR messages:", counts["ERROR"])
    print("Total log records:", len(data))

except FileNotFoundError:
    print("Error: logs.json file not found.")
except json.JSONDecodeError:
    print("Error: Invalid JSON data in logs.json.")
except ValueError as error:
    print(error)