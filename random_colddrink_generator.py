import tkinter as tk
import random

# List of cold drinks
cold_drinks_names = [
    "Iced Coffee",
    "Lemonade",
    "Iced Tea",
    "Smoothie",
    "Milkshake",
    "Cold Brew Coffee",
    "Soda",
    "Iced Latte",
    "Fruit Juice",
    "Sparkling Water",
    "Frappe",
    "Cold Chocolate",
    "Energy Drink",
    "Slushie",
    "Coconut Water",
    "Herbal Iced Tea"
]

def suggest_cold_drink():
    """Suggests a random cold drink and updates the label."""
    drink = random.choice(cold_drinks_names)
    result_label.config(text=f"How about a nice, refreshing {drink}?")

#  main window
root = tk.Tk()
root.title("Random Cold Drink Deciding Generator")


result_label = tk.Label(root, text="Click the button to get a drink suggestion!", font=("Helvetica", 16))
result_label.pack(pady=20)


suggest_button = tk.Button(root, text="Suggest a Drink", command=suggest_cold_drink, font=("Helvetica", 14))
suggest_button.pack(pady=10)

# Run the application
root.mainloop()
