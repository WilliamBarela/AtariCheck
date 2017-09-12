import csv
from IPython.core import debugger
debug = debugger.Pdb().set_trace
from cell import Cell


class Board(object):
    def __init__(self, board_size = 19):
        self.__board_size = board_size
        self.state = self.opening_state(board_size)

    def isValidState(self, state):
        instanceOfCell = [isinstance(j, Cell) for i in state for j in i]

        if not instanceOfCell or not all(instanceOfCell):
            raise ValueError("Invalid state: one or more cells is not an instance of Cell class")
        elif len(instanceOfCell) != self.board_size * self.board_size:
            raise ValueError("Invalid board size: insufficient cells instantiated")
        else:
            return True

    # FIXME: create rules for a valid stone placement
    def isValidMove(self, i, j, color):
        board = self.state
        cell = board[i][j]
        if (cell.isOnBoard(i) and cell.isOnBoard(j)) and cell.color is not None:
            raise ValueError("Stone has already been placed at %(r)s, %(c)s" % {"r": i, "c": j})
        #elif cell.isInAtari:
            # raise ValueError ("Invalid move: ko (suicide) would result")
        else:
            return True

    def opening_state(self, board_size):
        return [[Cell(i, j, board_size) for j in range(board_size)] for i in range(board_size)]

    @property
    def board_size(self):
        return self.__board_size

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, new_state):
        if self.isValidState(new_state): self.__state = new_state

    def place_stone(self, i, j, color):
        board = self.state
        cell = board[i][j]
        if self.isValidMove(i, j, color): 
            cell.color = None if color is "" else color 
            print "At: " + str(i) + ", " + str(j)  +  ": cell color: " + color
            cell.update_liberties_from_board(self.state)
        #return cell

    def import_board(self, csv_file = "csv/go.csv"):
        # be sure to include one more row in csv file
        with open(csv_file, 'rb') as rawCsv:
            readCsv = csv.reader(rawCsv)
            go = [row for row in readCsv]
            go.pop()
            if len(go) is not self.board_size or len(go[0]) is not self.board_size:
                raise ValueError("Imported data does not match board size.")
            return go

    def set_board(self, csv_file = "csv/go.csv"):
        board = self.import_board(csv_file)
        [[self.place_stone(i, j, board[i][j]) for j in range(len(board[0]))] for i in range(len(board))]

