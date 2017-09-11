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
    def isValidMove(i, j, color):
        return False
        # set rules (remember ko)
        # no stone may be placed if one is already placed

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

    # FIXME: create Cell.init_stone method
    def place_stone(i, j, color):
        cell = self.state[i][j]
        if self.isValidMove(i, j, color): cell.init_stone(color)
