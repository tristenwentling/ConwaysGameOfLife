from random import randint, choice


class Board(object):
    """create game of life arena"""

    def __init__(self, num=100):
        """initialize the arena"""
        self._sidelen = num
        self._size = num**2
        self.board = []
        self.errors = 0
        for i in range(num):
            row = []
            for j in range(num):
                col = [0]
                row.append(col)
            self.board.append(row)

    def show(self):
        """shows the board"""
        for i in range(self._sidelen):
            chars = ""
            for j in range(self._sidelen):
                if self.board[i][j][0] == 1:
                    chars = chars+"#"
                else:
                    chars = chars+"."
            print(chars)

    def toggle_val(self, row, col):
        """flips the value of an entry"""
        x = self.board[row][col][0]
        if x == 0:
            self.board[row][col][0] = 1
        elif x == 1:
            self.board[row][col][0] = 0
        else:
            self.errors += 1
