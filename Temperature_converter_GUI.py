import tkinter as tk
from tkinter import ttk, messagebox

# Function to convert temperature
def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            c = temp
            f = (c * 9 / 5) + 32
            k = c + 273.15
        elif unit == "Fahrenheit":
            f = temp
            c = (f - 32) * 5 / 9
            k = c + 273.15
        elif unit == "Kelvin":
            k = temp
            c = k - 273.15
            f = (c * 9 / 5) + 32
        else:
            raise ValueError("Invalid unit selected")

        result_label.config(
            text=f"Results:\nCelsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# GUI Window setup
root = tk.Tk()
root.title("Temperature Converter - Prodigy InfoTech Task-01")
root.geometry("400x350")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Temperature Converter", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Temperature input
entry_label = tk.Label(root, text="Enter Temperature:", font=("Helvetica", 12), bg="#f0f0f0")
entry_label.pack()
entry_temp = tk.Entry(root, font=("Helvetica", 12), width=20, justify='center')
entry_temp.pack(pady=5)

# Unit selection
unit_label = tk.Label(root, text="Select Unit:", font=("Helvetica", 12), bg="#f0f0f0")
unit_label.pack()
combo_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Helvetica", 12), state="readonly")
combo_unit.pack(pady=5)
combo_unit.set("Celsius")

# Convert Button
convert_btn = tk.Button(root, text="Convert", command=convert_temperature, font=("Helvetica", 12), bg="#4CAF50", fg="white")
convert_btn.pack(pady=15)


result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0", justify="center")
result_label.pack()


root.mainloop()
