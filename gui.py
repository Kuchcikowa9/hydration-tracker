import tkinter as tk
from main import add_water, show_today_summary

# Main window

root = tk.Tk()
root.title("Hydration tracker 💧")
root.geometry("300x200")

# Add water funktion

def handle_add_water():
    amount = amount_entry.get()
    if amount.isdigit():
        add_water(int(amount))
        amount_entry.delete(0, tk.END)
    else:
        result_label.config(text="Please enter a valid number")

# Show today's summary

def handle_show_summary():
    show_today_summary()

# Entry for amount

amount_label = tk.Label(root, text="Enter water amount (ml):")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

add_button = tk.Button(root, text="Add water", command=handle_add_water)
add_button.pack(pady=5)

summary_button = tk.Button(root, text="Show Summary", command=handle_show_summary)
summary_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

# Start GUI

root.mainloop()