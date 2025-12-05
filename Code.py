import os
from datetime import datetime

data_file = "courier_data.txt"

def validate_tracking_id(tracking_id):
    return len(tracking_id) >= 8 and len(tracking_id) <= 12 and tracking_id.isalnum()

def add_c():
    while True:
        track_id = input("Enter Tracking ID (8-12 alphanumeric chars): ")
        if validate_tracking_id(track_id):
            break
        print("Invalid Tracking ID. Must be 8-12 alphanumeric characters.\n")

    sender = input("Enter Sender Name: ").strip()
    receiver = input("Enter Receiver Name: ").strip()
    status = "In Transit"
    created_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(data_file, "a") as f:
        f.write(f"{track_id},{sender},{receiver},{status},{created_date}\n")

    print("Courier added successfully!\n")

def update_c():
    track_id = input("Enter Tracking ID to update: ")

    if not os.path.exists(data_file):
        print("No courier records found.")
        return

    updated = False
    lines = []

    with open(data_file, "r") as f:
        lines = f.readlines()

    with open(data_file, "w") as file:
        for line in lines:
            data = line.strip().split(",")
            if len(data) >= 5 and data[0] == track_id:
                new_status = input("Enter new status: ").strip()
                data[3] = new_status
                data[4] = datetime.now().strftime("%Y-%m-%d %H:%M")
                updated = True
                file.write(",".join(data) + "\n")
            else:
                file.write(line)

    print("Status updated successfully!" if updated else "Tracking ID not found.\n")

def delete_c():
    track_id = input("Enter Tracking ID to delete: ")

    if not os.path.exists(data_file):
        print("No courier records found.")
        return

    lines = []
    deleted = False

    with open(data_file, "r") as file:
        lines = file.readlines()

    with open(data_file, "w") as file:
        for line in lines:
            if line.strip().split(",")[0] != track_id:
                file.write(line)
            else:
                deleted = True

    print("Courier deleted successfully!" if deleted else "Tracking ID not found.\n")

def search_c():
    search_term = input("Enter name or Tracking ID to search: ").lower().strip()

    if not os.path.exists(data_file):
        print("No courier records found.")
        return

    print("\n--- Search Results ---")
    found = False

    with open(data_file, "r") as file:
        for line_num, line in enumerate(file, 1):
            data = line.strip().split(",")
            if (search_term in data[0].lower() or
                search_term in data[1].lower() or
                search_term in data[2].lower()):
                print(f"Line {line_num}: ID:{data[0]} | {data[1]} -> {data[2]} | {data[3]} | {data[4]}")
                found = True

    if not found:
        print("No matching records found.\n")

def track_c():
    track_id = input("Enter Tracking ID to track: ")

    if not os.path.exists(data_file):
        print("No courier records found.")
        return

    found = False

    with open(data_file, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) >= 5 and data[0] == track_id:
                print("\n----- Courier Details -----")
                print("Tracking ID    :", data[0])
                print("Sender         :", data[1])
                print("Receiver       :", data[2])
                print("Status         :", data[3])
                print("Last Updated   :", data[4])
                print("----------------------------\n")
                found = True
                break

    if not found:
        print("Tracking ID not found.\n")

def display():
    if not os.path.exists(data_file):
        print("No courier records found.")
        return

    print("\n===== All Courier Records =====")
    with open(data_file, "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(f"ID:{data[0]} | {data[1]} -> {data[2]} | {data[3]} | {data[4]}")
    print("================================\n")

def main():
    while True:
        print("\n====== COURIER TRACKING SYSTEM ======")
        print("1.  Add Courier")
        print("2.  Update Courier Status")
        print("3.  Track Courier")
        print("4.  View All Couriers")
        print("5.  Search Couriers")
        print("6.  Delete Courier")
        print("7.  Exit")
        print("=====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_c()
        elif choice == "2":
            update_c()
        elif choice == "3":
            track_c()
        elif choice == "4":
            display()
        elif choice == "5":
            search_c()
        elif choice == "6":
            delete_c()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
