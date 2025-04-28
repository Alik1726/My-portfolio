import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.current_player = 'X'
        self.game_mode = 'Two Player'  # Default to two-player mode
        
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text='', width=10, height=3, font=("Arial", 24),
                                               command=lambda i=i, j=j: self.click(i, j))
                self.buttons[i][j].grid(row=i, column=j)
        
        # Game Mode Buttons
        self.game_mode_button = tk.Button(root, text="Switch to Computer Mode", command=self.toggle_game_mode)
        self.game_mode_button.grid(row=3, column=0, columnspan=3, pady=20)

    def toggle_game_mode(self):
        if self.game_mode == 'Two Player':
            self.game_mode = 'Player vs Computer'
            self.game_mode_button.config(text="Switch to Two Player Mode")
            messagebox.showinfo("Game Mode", "You are playing against the computer now!")
        else:
            self.game_mode = 'Two Player'
            self.game_mode_button.config(text="Switch to Computer Mode")
            messagebox.showinfo("Game Mode", "You are playing against another player now!")

    def click(self, i, j):
        if self.board[i][j] is None:  # If the spot is empty
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()
                
                # If it's the computer's turn in Player vs Computer mode
                if self.game_mode == 'Player vs Computer' and self.current_player == 'O':
                    self.computer_move()

    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != None:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != None:
            return True
        return False

    def is_board_full(self):
        # Check if the board is full
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    return False
        return True

    def switch_player(self):
        # Switch the current player
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def computer_move(self):
        # Simple AI: Random move for the computer
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
        if available_moves:
            move = random.choice(available_moves)
            i, j = move
            self.board[i][j] = 'O'
            self.buttons[i][j].config(text='O')

            if self.check_winner():
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.switch_player()

    def reset_game(self):
        # Reset the game board and UI
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
        self.current_player = 'X'

# Create the main window
root = tk.Tk()

# Create the TicTacToe game object
game = TicTacToe(root)

# Run the game
root.mainloop()
