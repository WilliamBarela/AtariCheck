class Cell(object):
    def __init__(self, i, j, board_size):
        self.board_size = board_size
        self.i = i
        self.j = j
        self.color = None
        self.display = " "
        self.__liberties = self.init_liberties()
        # add liberties

    def isValidBoardSize(self, board_size):
        if not isinstance(board_size, int) or board_size < 0:
            raise ValueError("Board must be a non-negative integer")
        if hasattr(self, "board_size"):
            raise ValueError("Board size cannot be reset")
        else:
            return True

    def isOnBoard(self, iterator):
        if not (iterator >= 0 and iterator < self.board_size):
            raise ValueError("i or j coordinate is invalid.")
        else:
            return True

    def isValidColor(self, color):
        valid_colors = [None, "black", "white"]

        if color not in valid_colors:
            raise ValueError("Color invalid: (choose: None, black, or white)")
        elif hasattr(self, "color") and self.color is not None:
            raise ValueError("Color cannot be changed once set")
        else:
            return True

    def isLiberty(self, liberty):
        valid_liberties = ["edge", None, "black", "white"]

        if liberty not in valid_liberties:
            raise ValueError("Liberty invalid: (choose: edge, None, black or White.)")
        else:
            return True
    
    def isValidNLiberty(self, N):
        if self.isLiberty(N):
            if self.i == 0 and N is not "edge":
                raise ValueError("N liberty in 0th row must be set to 'edge'")
            elif self.i > 0 and N is "edge":
                raise ValueError("N liberty can only be 'edge' in 0th row")
            else:
                return True
    
    def isValidSLiberty(self, S):
        if self.isLiberty(S):
            if self.i == (self.board_size - 1) and S is not "edge":
                raise ValueError("S liberty in last row must be set to 'edge'")
            elif self.i < (self.board_size - 1) and S is "edge":
                raise ValueError("S liberty can only be 'edge' in last row")
            else:
                return True

    def isValidWLiberty(self, W):
        if self.isLiberty(W):
            if self.j == 0 and W is not "edge":
                raise ValueError("W liberty in 0th column must be set to 'edge'")
            elif self.j > 0 and W is "edge":
                raise ValueError("W liberty can only be 'edge' in 0th column")
            else:
                return True
    
    def isValidELiberty(self, E):
        if self.isLiberty(E):
            if self.j == (self.board_size - 1) and E is not "edge":
                raise ValueError("E liberty in last column must be set to 'edge'")
            elif self.j < (self.board_size - 1) and E is "edge":
                raise ValueError("E liberty can only be 'edge' in last column")
            else:
                return True

    @property
    def board_size(self):
        return self.__board_size

    @board_size.setter
    def board_size(self, board_size):
        if self.isValidBoardSize(board_size): self.__board_size = board_size

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

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if self.isValidColor(color): 
            self.__color = color
            self.display = self.color

    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, color):
        black = u'\u25CB'
        white = u'\u25CF'
        blank = " "

        if color == "black":
            self.__display = black
        elif color == "white":
            self.__display = white
        else:
            self.__display = blank

    @property
    def liberties(self):
        self.update_liberties()
        return self.__liberties

    def update_liberties_from_board(self, board):
        # sets N liberty for self and adjacent cell
        if self.i == 0:
            self.N = "edge" 
        else:
            cellN = board[self.i - 1][self.j]
            self.N = cellN.color
            cellN.S = self.color

        # sets S liberty for self and adjacent cell
        if self.i == (self.board_size - 1):
            self.S = "edge"
        else:
            cellS = board[self.i + 1][self.j]
            self.S = cellS.color 
            cellS.N = self.color

        # sets W liberty for self and adjacent cell
        if self.j == 0:
            self.W = "edge" 
        else:
            cellW = board[self.i][self.j - 1]
            self.W = cellW.color
            cellW.E = self.color

        # sets E liberty for self and adjacent cell
        if self.j == (self.board_size - 1):
            self.E = "edge"
        else:
            cellE = board[self.i][self.j + 1]
            self.E = cellE.color
            cellE.W = self.color

        self.update_liberties()

    def update_liberties(self):
        self.__liberties = {"north": self.N, "south": self.S, "west": self.W, "east": self.E}

    def init_liberties(self):
        self.N = "edge" if self.i == 0 else None
        self.S = "edge" if self.i == (self.board_size - 1) else None 
        self.W = "edge" if self.j == 0 else None
        self.E = "edge" if self.j == (self.board_size - 1) else None
        
        return {"north": self.N, "south": self.S, "west": self.W, "east": self.E}

    @property
    def N(self):
        return self.__N

    @N.setter
    def N(self, N):
        if self.isValidNLiberty(N): self.__N = N
    
    @property
    def S(self):
        return self.__S

    @S.setter
    def S(self, S):
        if self.isValidSLiberty(S): self.__S = S

    @property
    def W(self):
        return self.__W

    @W.setter
    def W(self, W):
        if self.isValidWLiberty(W): self.__W = W

    @property
    def E(self):
        return self.__E

    @E.setter
    def E(self, E):
        if self.isValidELiberty(E): self.__E = E
