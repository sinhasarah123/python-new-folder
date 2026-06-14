import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        # Simple Interest
        si = (p * t * r) / 100

        # Compound Interest
        amount = p * ((1 + r / 100) ** t)
        ci = amount - p

        result_label.config(
            text=f"Simple Interest = {si:.2f}\nCompound Interest = {ci:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x250")

tk.Label(root, text="Principal Amount").pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

tk.Label(root, text="Time Period (Years)").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Label(root, text="Rate of Interest (%)").pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()