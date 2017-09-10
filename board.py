class Board(object):
    def __init__(self, board_size = 19):
        self.__board_size = board_size
        self.state = self.opening_state(board_size)

    def opening_state(self, board_size):
        # replace "cell" with cell data structure:
        return [["cell" for j in range(board_size)] for i in range(board_size)]

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, new_state):
        instanceOfCell = [j == "cell" for i in new_state for j in i]
        if not instanceOfCell: instanceOfCell = [False] # checks if empty set
        if all(instanceOfCell): self.__state = new_state
