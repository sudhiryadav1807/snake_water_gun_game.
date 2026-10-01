import tkinter as tk
import random

# Game window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("450x550")
root.configure(bg="#172554")
root.resizable(False, False)

# Scores
player_score = 0
computer_score = 0

choices = ["Snake", "Water", "Gun"]

# Winner logic
def play(user_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    player_label.config(text=f"You: {user_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a Draw!", fg="yellow")

    elif (
        (user_choice == "Snake" and computer_choice == "Water")
        or (user_choice == "Water" and computer_choice == "Gun")
        or (user_choice == "Gun" and computer_choice == "Snake")
    ):
        player_score += 1
        result_label.config(text="You Win! 🎉", fg="#4ade80")

    else:
        computer_score += 1
        result_label.config(text="You Lose! 😢", fg="#f87171")

    score_label.config(
        text=f"Your Score: {player_score}   |   Computer: {computer_score}"
    )

# Reset game
def reset():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    player_label.config(text="You: -")
    computer_label.config(text="Computer: -")
    result_label.config(text="Choose your move!", fg="white")
    score_label.config(text="Your Score: 0   |   Computer: 0")

# Heading
title = tk.Label(
    root, text="🐍 Snake Water Gun 💧",
    font=("Arial", 20, "bold"),
    bg="#172554", fg="white"
)
title.pack(pady=25)

# Instructions
tk.Label(
    root, text="Choose your weapon!",
    font=("Arial", 14),
    bg="#172554", fg="white"
).pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#172554")
button_frame.pack(pady=15)

for name, emoji in [
    ("Snake", "🐍"),
    ("Water", "💧"),
    ("Gun", "🔫")
]:
    tk.Button(
        button_frame,
        text=f"{emoji}\n{name}",
        font=("Arial", 13, "bold"),
        width=9,
        height=3,
        bg="#2563eb",
        fg="white",
        command=lambda n=name: play(n)
    ).pack(side="left", padx=5)

# Result
player_label = tk.Label(
    root, text="You: -",
    font=("Arial", 14),
    bg="#172554", fg="white"
)
player_label.pack(pady=12)

computer_label = tk.Label(
    root, text="Computer: -",
    font=("Arial", 14),
    bg="#172554", fg="white"
)
computer_label.pack(pady=5)

result_label = tk.Label(
    root, text="Choose your move!",
    font=("Arial", 18, "bold"),
    bg="#172554", fg="white"
)
result_label.pack(pady=20)

# Scoreboard
score_label = tk.Label(
    root, text="Your Score: 0   |   Computer: 0",
    font=("Arial", 13, "bold"),
    bg="#172554", fg="#93c5fd"
)
score_label.pack(pady=15)

# Reset button
tk.Button(
    root, text="🔄 Reset Game",
    font=("Arial", 12, "bold"),
    bg="#16a34a", fg="white",
    command=reset
).pack(pady=15)

root.mainloop()