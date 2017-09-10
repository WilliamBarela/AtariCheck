class Board:
    def __init__(self, board_size = 19):
        self.__board_size = board_size
        self.state = self.opening_state(board_size)

    def opening_state(self, board_size):
        # replace "cell" with cell data structure:
        return [["cell" for j in range(board_size)] for i in range(board_size)]

