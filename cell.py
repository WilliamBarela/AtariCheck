class Cell(object):
    def __init__(self, i, j, board_size):
        self._board_size = board_size
        self.i = i
        self.j = j
        # make setters and getters for i and j
        # add liberties

    def isOnBoard(self, iterator):
        if not (iterator >= 0 and iterator < self._board_size):
            raise ValueError("i or j coordinate is invalid.")
        else:
            return True

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, i):
        if self.isOnBoard(i): self.__i = i

    @property
    def j(self):
        return self.__j

    @j.setter
    def j(self, j):
        if self.isOnBoard(j): self.__j = j

