import tkinter as tk
from tkinter import messagebox
import random

current_player = "X"
board = [""] * 9 
buttons = []
game_over = False

def create_window():
    window = tk.Tk()
    window.title("Tic-Tac-Toe Game")
    window.geometry("400x550")
    window.resizable(False,False)
    return window

def create_game_board(window):
    global buttons
    board_frame = tk.Frame(window)
    board_frame.pack(pady = 10)

    for i in range(9):
        row = i//3
        col = i%3 
        button = tk.Button(board_frame, text = "", width = 6, height = 3, font = ("Verdana",20,"bold"), bg = "light blue", command = lambda pos=i: button_click(pos))
        button.grid(row = row, column = col, padx = 2, pady = 2)
        buttons.append(button)

def check_winner():
    global game_over
    winning_combinations = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for comb in winning_combinations:
        if board[comb[0]] == board[comb[1]] == board[comb[2]] != "":
            game_over = True
            messagebox.showinfo("Game Over", f"Player {board[comb[0]]} wins!")
            status_label.config(text=f"Player {board[comb[0]]} wins!")
            return True
    if "" not in board:
        game_over = True
        messagebox.showinfo("Game Over", "It's a Tie!")
        status_label.config(text="It's a Tie!")
        return True
    return False

def create_controls(window):
    global status_label
    status_label = tk.Label(window, text = "Current Player: X", font = ("Arial", 14))
    status_label.pack(pady=10)
    reset_btn = tk.Button(window, text="Reset", font=("Arial", 12), command=reset_game)
    reset_btn.pack(pady=5)

def reset_game():
    global board, current_player, game_over
    board = [""] * 9
    current_player = random.choice(["X", "O"])
    game_over = False
    for btn in buttons:
        btn.config(text="", state="normal")
    status_label.config(text=f"Current Player: {current_player}")


def button_click(position):
    global current_player, game_over
    if game_over or board[position] != "":
        return
    board[position] = current_player
    buttons[position].config(text = current_player, state = "disabled")
    if not check_winner():
        current_player = "O" if current_player == "X" else "X"
        status_label.config(text=f"Current Player: {current_player}")

def main():
    global current_player
    current_player = random.choice(["X", "O"])
    root = create_window()
    title_label = tk.Label(root, text = "Tic-Tac-Toe", font = ("Courier New",16,"bold"))
    title_label.pack(pady = 10)
    create_controls(root)
    create_game_board(root)
    status_label.config(text=f"Current Player: {current_player}")
    root.mainloop()


main()

