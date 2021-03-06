from board import Board
from random import randint
from math import floor


class LifeGame(Board):
    """runs Conway's 'Game of Life' """

    def __init__(self, num=100, set_params=True):
        """instantiation of the g.o.l. board"""
        self._iternum = 100  # updateable option
        self._sidelen = num  # updateable option
        self._size = num**2
        self._step_size = 1  # updateable option
        self._batch_size = 0  # updateable option
        self._num_batches = 1  # will be set if set_params is run later
        self.board = []
        if set_params:
            self.set_alt_params()
        for i in range(num):
            row = []
            for j in range(num):
                col = [0]
                row.append(col)
            self.board.append(row)
        self._temp_board = list(self.board)
        for j in range(10000):
            x = randint(0, num-1)
            y = randint(0, num-1)
            self.toggle_val(x, y)
        self.show()

    def run_game(self, rule="original"):
        """runs one timestep of the game"""
        for i in range(self._sidelen):
            for j in range(self._sidelen):
                cur_val = self.board[i][j][0]
                target = (i, j)
                values = self.check_squares(target)
                count = self.counter(values)
                its_alive = (count == 3)
                stayin_alive = (count == 2) or (count == 3)
                dead = (cur_val == 0)
                alive = (cur_val == 1)
                if (dead and its_alive):
                    self.set_val(i, j, 1)
                elif (alive and stayin_alive):
                    self.set_val(i, j, 1)
                else:
                    self.set_val(i, j, 0)
        self.board = list(self._temp_board)

    def counter(self, values):
        """counts True entries in list/dict/set"""
        xxx = 0
        for i in values:
            if i:
                xxx += 1
        return xxx

    def set_val(self, x, y, val):
        """updates value on temporary board"""
        self._temp_board[x][y][0] = val

    def get_board_state(self):
        """catchs current board state"""
        return self.board

    def check_squares(self,i,j):
        try:
            up = self.board[i-1][j][0]
        except IndexError:
            up = False
        try:
            down = self.board[i-1][j][0]
        except IndexError:
            down = False
        try:
            left = self.board[i-1][j][0]
        except IndexError:
            left = False
        try:
            right = self.board[i][j+1][0]
        except IndexError:
            right = False
        try:
            upleft = self.board[i-1][j-1][0]
        except IndexError:
            upleft = False
        try:
            downright = self.board[i+1][j+1][0]
        except IndexError:
            downright = False
        try:
            downleft = self.board[i+1][j-1][0]
        except IndexError:
            downleft = False
        try:
            upright = self.board[i-1][j+1][0]
        except IndexError:
            upright = False
        values = [up, down, left, right,
                  upleft, upright, downleft, downright]
        return values

    def set_alt_params(self):
        def_file = open("params.txt", "r")
        lines = def_file.readlines()
        params = lines[0].split(',')
        self._iternum = int(params[0])
        self._batch_size = int(params[1])
        self._sidelen = int(params[2])
        self._step_size = int(params[3])
        self._num_batches = int(self._iternum/self._batch_size)+1
