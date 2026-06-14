import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(player_choice):
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)

# Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x250")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
title.pack(pady=10)

rock_btn = tk.Button(root, text="Rock", width=10,
                     command=lambda: play("Rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper", width=10,
                      command=lambda: play("Paper"))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors", width=10,
                         command=lambda: play("Scissors"))
scissors_btn.pack(pady=5)

computer_label = tk.Label(root, text="")
computer_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()