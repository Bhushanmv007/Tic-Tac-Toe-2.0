import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe with a Twist")
        
        # Initialize game state
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.moves = {"X": [], "O": []}  # Stores moves for each player
        self.turn_count = {"X": 0, "O": 0}  # Count turns for each player
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Create buttons
        for i in range(3):
            for j in range(3):
                button = tk.Button(root, text="", font=('normal', 40, 'bold'), width=5, height=2,
                                   command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_click(self, i, j):
        if self.buttons[i][j]["text"] == "" and not self.check_winner():
            # Update the board and button text
            self.board[i][j] = self.current_player
            self.buttons[i][j]["text"] = self.current_player
            self.moves[self.current_player].append((i, j))
            self.turn_count[self.current_player] += 1
            
            # Check if it's the 4th turn and remove the 1st move
            if self.turn_count[self.current_player] == 4:
                self.remove_first_move()

            # Check for a winner
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.switch_player()

    def remove_first_move(self):
        # Remove the first move of the current player
        if self.moves[self.current_player]:
            first_move = self.moves[self.current_player].pop(0)
            self.board[first_move[0]][first_move[1]] = ""
            self.buttons[first_move[0]][first_move[1]]["text"] = ""

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
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

    def is_draw(self):
        # Check if all cells are filled
        for row in self.board:
            if "" in row:
                return False
        return True

    def reset_board(self):
        # Reset the game for a new round
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.moves = {"X": [], "O": []}
        self.turn_count = {"X": 0, "O": 0}
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
