class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        """
        Draw the board of Tic-Tac-Toe game
        """
        for row in range(3): # based on the number of row, create 2 lines repetitively
            print(" ---" * 3)
            print("|", end="") # start with one |, not changing line
            for col in range(3): # based on the number of col, fill in the matrix
                if (self.grid[row][col] == ""):
                    print("   |", end="")
                else:
                    print(f" {self.grid[row][col]} |", end="")
                print() # change line
        print(" ---" * 3) # finalize with the last line

    def update_board(self, row: int, col: int, symbol: str) -> bool:
        """
        Update the game board based on location selected by player

        Args:
            row (int): row index of board
            col (int): column index of board
            symbol (str): symbol used by player
        """
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self) -> str:
        """
        Check the winner of the current board

        Returns:
            str: The winning symbol ('X' or 'O') if there is a winner, else an empty string
        """
        draw = 1

        for row in range(3):
            if row[0] == row[1] == row[2] and row[0] != "": # to prevent the whole row is empty
                draw = 0
                return row[0]
            
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] != "": # to prevent the whole col is empty
                draw = 0
                return self.grid[0][col]
        
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != "": # to prevent the whole diagonal line is empty
            draw = 0
            return self.grid[0][0]
        
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != "": # to prevent the whole diagonal line is empty
            draw = 0
            return self.grid[0][2]
        
        if draw == 0:
            draw = 1
            return ""

    def is_full(self) -> bool:
        """
        Check if the current board is full or not

        Returns:
            bool: Boolean outcome indicating whether the board is full
        """
        return all(cell != " " for row in self.grid for cell in row)
