import tkinter as tk
import random

def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or          (user_choice == "Paper" and computer_choice == "Rock") or          (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors - CodSoft Task 4")
root.geometry("400x280")
root.configure(bg="lightblue")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="lightblue")
title.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue", justify="center")
result_label.pack(pady=20)

button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack()

choices = ["Rock", "Paper", "Scissors"]
for choice in choices:
    btn = tk.Button(button_frame, text=choice, font=("Arial", 14), width=10,
                    command=lambda c=choice: play(c))
    btn.pack(side="left", padx=10)

root.mainloop()
