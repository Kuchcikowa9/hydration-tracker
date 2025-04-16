import json
from datetime import datetime

def add_water(amount_ml):
    now = datetime.now()
    entry = {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "amount_ml": amount_ml
    }

    try:
        with open("data/log.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open("data/log.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Added {amount_ml} ml of water!")

def load_data():
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

