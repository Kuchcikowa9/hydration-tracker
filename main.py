import json
from datetime import datetime

def add_water(amount_ml):
    # Get current date and time
    now = datetime.now()
    
    # Create a new water intake entry
    entry = {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "amount_ml": amount_ml
    }

    # Load existing data from JSON (if it exists)
    try:
        with open("data/log.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    # Add the new entry to the list
    data.append(entry)

    # Save updated data back to JSON
    with open("data/log.json", "w") as f:
        json.dump(data, f, indent=4)

    # Confirmation message
    print(f"Added {amount_ml} ml of water!")

# Example usage
add_water(250)
