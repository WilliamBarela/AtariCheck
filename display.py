from board import Board
from cell import Cell
from os import system

class Display(Board):
    def __init__(self, board_size):
        Board.__init__(self, board_size)
        self.clear_screen()
        self.board()

    def board(self):
        m_dash = "---"
        divider = "---|" + "|".join([m_dash for cell in range(self.board_size)])
        
        print "   |" + "|".join(["%3s" % (i) for i in range(self.board_size)])
        print divider
        for i, row in enumerate(self.state):
            row_num_formatted = "%2s" % (i) 
            print row_num_formatted + " |" + " |".join([" " + cell.display for cell in row]) + " |"
            print divider 

    def clear_screen(self):
        system("clear || cls")

    def place_stone(self, i, j, color):
        super(Display, self).place_stone(i, j, color)
        self.clear_screen()
        self.board()
