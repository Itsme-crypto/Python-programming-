import tkinter as tk
import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def on_button_click(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_var.set(f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

tk.Label(root, text="Choose rock, paper, or scissors:").pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", command=lambda: on_button_click("rock")).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Paper", command=lambda: on_button_click("paper")).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Scissors", command=lambda: on_button_click("scissors")).pack(side=tk.LEFT, padx=5)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).pack(pady=10)

root.mainloop()