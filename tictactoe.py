import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Main game class
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe with a Twist")
        
        # Background gradient color
        self.root.configure(bg='#1e1e2f')
        
        # Game variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.move_lists = {"X": [], "O": []}  # Track moves for each player

        # Custom font
        self.custom_font = font.Font(family="Arial", size=24, weight="bold")

        # Create buttons with enhanced UI
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    root, text="", font=self.custom_font, width=5, height=2,
                    bg='#3e4a61', fg='#f5f5f5', activebackground='#5a6b82', 
                    activeforeground='#f0f0f0', borderwidth=0, 
                    command=lambda i=i, j=j: self.button_click(i, j)
                )
                self.buttons[i][j].grid(row=i, column=j, padx=10, pady=10)
                
    def button_click(self, i, j):
        if self.buttons[i][j]["text"] == "" and self.check_winner() is False:
            self.buttons[i][j]["text"] = self.current_player
            self.board[i][j] = self.current_player
            self.move_lists[self.current_player].append((i, j))

            # Check if the move needs to discard any previous move
            if len(self.move_lists[self.current_player]) % 4 == 0:
                self.discard_move(self.current_player)

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def discard_move(self, player):
        # Determine which move to discard
        move_index = len(self.move_lists[player]) - 4
        if move_index >= 0:
            discard_move = self.move_lists[player][move_index]
            discard_i, discard_j = discard_move
            self.board[discard_i][discard_j] = ""
            self.buttons[discard_i][discard_j]["text"] = ""
            self.move_lists[player].pop(move_index)

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.move_lists = {"X": [], "O": []}  # Reset move lists
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""

# Running the game
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
