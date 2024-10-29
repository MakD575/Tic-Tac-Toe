import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.board = [""] * 9
        self.current_player = ""
        self.ai_player = "O"  # AI is "O"

        self.mode = self.choose_mode()
        self.choose_player()

        self.buttons = [tk.Button(master, text="", font=("Arial", 24), width=5, height=2,
                                  command=lambda i=i: self.make_move(i)) for i in range(9)]

        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)

    def choose_mode(self):
        mode = messagebox.askquestion("Choose Mode",
                                      "Do you want to play against the computer? (Yes = AI, No = Player 2)")
        return mode == "yes"

    def choose_player(self):
        self.player_choice = messagebox.askquestion("Choose Player", "Do you want to be X? (Yes = X, No = O)")
        self.current_player = "X" if self.player_choice == "yes" else "O"
        self.ai_player = "O" if self.current_player == "X" else "X"

    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.show_winner(self.current_player)
            else:
                if self.mode and self.current_player == "X":  # If player is X, switch to AI
                    self.current_player = self.ai_player
                    self.ai_move()
                else:  # Switch to Player 2
                    self.current_player = "X" if self.current_player == "O" else "O"

    def ai_move(self):
        available_moves = [i for i in range(9) if self.board[i] == ""]
        if available_moves:
            move = random.choice(available_moves)
            self.board[move] = self.ai_player
            self.buttons[move].config(text=self.ai_player)
            if self.check_winner():
                self.show_winner(self.ai_player)
            else:
                self.current_player = "X" if self.player_choice == "yes" else "O"

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]  # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def show_winner(self, winner):
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_game()

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.choose_player()  # Ask player to choose X or O again
        self.mode = self.choose_mode()  # Ask for mode again


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


