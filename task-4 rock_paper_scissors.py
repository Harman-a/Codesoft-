import tkinter as tk
import random

user_score = 0
comp_score = 0

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors") or
        (user_choice == "Paper" and comp_choice == "Rock") or
        (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        user_score += 1
        result = "You Win!"
    else:
        comp_score += 1
        result = "Computer Wins!"

    user_choice_label.config(text=f"Your Choice: {user_choice}")
    comp_choice_label.config(text=f"Computer's Choice: {comp_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score}  Computer: {comp_score}")

def reset():
    user_choice_label.config(text="Your Choice: ")
    comp_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x350")

title_label = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_choice_label.pack()

comp_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12))
comp_choice_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0  Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.pack(side=tk.LEFT, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.pack(side=tk.LEFT, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.pack(side=tk.LEFT, padx=5)

reset_btn = tk.Button(root, text="Play Again", command=reset)
reset_btn.pack(pady=10)

root.mainloop()
