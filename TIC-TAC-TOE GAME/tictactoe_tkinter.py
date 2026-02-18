
import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Variables
current_player = "X"
board = [""] * 9
buttons = []

# Function to check winner
def check_winner():
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]
    return None

# Function when button is clicked
def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index]["text"] = current_player

        winner = check_winner()

        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Reset game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for button in buttons:
        button["text"] = ""

# Create buttons (3x3 grid)
for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Run the window
root.mainloop()
