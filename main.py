import json
from datetime import datetime
from collections import defaultdict

def add_water(amount_ml):
    # Get current date and time
    now = datetime.now()
    entry = {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "amount_ml": amount_ml
    }

    try:
        # Load existing data from the JSON file
        with open("data/log.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    # Add new entry to the data list
    data.append(entry)

    # Save the updated data back to the JSON file
    with open("data/log.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Added {amount_ml} ml of water!")

def load_data():
    # Load data from the JSON file
    try:
        with open("data/log.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def get_today_total(data):
    today = datetime.now().date()
    total = 0
    for entry in data:
        entry_date = datetime.strptime(entry["date"], "%Y-%m-%d").date()
        if entry_date == today:
            total += entry["amount_ml"]
    return total

def show_today_summary():
    # Load data from the JSON file
    data = load_data()  
    
    # Get the total water intake for today
    today_total = get_today_total(data)  
    
    # Display a message based on the total water intake
    if today_total == 0:
        print("You haven't logged any water today 😟 Don't forget to hydrate!")
    elif today_total < 1000:
        print(f"You've had {today_total} ml today 💧 Keep going!")
    elif today_total < 2000:
        print(f"You've had {today_total} ml today 💪 Nice job — you're getting there!")
    else:
        print(f"You've had {today_total} ml today 🥳 Great work, you're well hydrated!")

    from collections import defaultdict

def get_monthly_summary(data):
    today = datetime.now()
    current_month = today.strftime("%Y-%m")
    summary = defaultdict(int)

    for entry in data:
        entry_date = entry["date"]
        if entry_date.startswith(current_month):
            summary[entry_date] += entry["amount_ml"]

    return dict(summary)

def show_monthly_summary():
    data = load_data()
    monthly = get_monthly_summary(data)

    if not monthly:
        print("No data for this month yet.")
        return

    print("\n💧 Monthly Water Intake Summary:\n")
    for date in sorted(monthly):
        print(f"{date} — {monthly[date]} ml")
    print()


def menu():
    while True:
        print("\n--- Hydration Tracker ---")
        print("1. Add water")
        print("2. Show today's summary")
        print("3. Show monthly summary")  # NEW
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            amount_ml = int(input("How much water did you drink (in ml)? "))
            add_water(amount_ml)
        elif choice == "2":
            show_today_summary()
        elif choice == "3":
            show_monthly_summary()  # NEW
        elif choice == "4":
            print("Goodbye! Stay hydrated! 💧")
            break
        else:
            print("Invalid option, please choose again.")


# Start the menu
menu()