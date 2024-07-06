import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg='light grey')
        self.board = [" " for _ in range(9)]  # Initialize empty board
        self.current_player = "X"  # X starts the game
        self.buttons = []  # List to store button widgets

        self.create_widgets()

    def create_widgets(self):
        # Heading
        self.heading = tk.Label(self.root, text="Tic Tac Toe", font='Arial 24 bold', bg='light grey')
        self.heading.grid(row=0, column=0, columnspan=3)

        # Create board
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.root, text=" ", font='Arial 20 bold', width=5, height=2,
                                   command=lambda r=row, c=col: self.handle_click(r, c), bg='white')
                button.grid(row=row+1, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset", font='Arial 14', command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)

    def handle_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_move()

    def computer_move(self):
        empty_indices = [i for i, x in enumerate(self.board) if x == " "]
        if empty_indices:
            index = random.choice(empty_indices)
            row, col = divmod(index, 3)
            self.board[index] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "X"

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return True
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
