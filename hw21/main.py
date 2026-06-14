import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)

    if length < 6:
        result.config(text="Weak Password")
    elif length < 10:
        result.config(text="Medium Password")
    else:
        result.config(text="Strong Password")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

tk.Label(root, text="Enter Password:").pack(pady=10)

entry = tk.Entry(root, show="*")
entry.pack()

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()