# AtariCheck (Python 2.7)
### AtariCheck is currently a work in progress
This repo was inspired by a whiteboard interview question which posed the question of how to best find all groups on a Go board which are in atari.

Currently, board.py, cell.py, and display.py form the basis of an API for generating and displaying a Go board of any positive dimension (defaults to 19 x 19). One can also use the import_board() method to import a preset board from a csv file. Once the board/display is instantiated, stones may be placed on the board which then updates the display.  This small and simple API utilizes OOP (including encapsulation, inheritance, etc.), data structures to represent complex information, and data validation to avoid invalid inputs. 

Future features planned to extend this project include the addition of a CLI class, better rule checking (for "ko"), a method which finds all contiguous groups of a certain color, and of course a method which displays with a warning color any group in atari on the board.

## API usage:
### Import Display and instantiate a board:
  ```py
      from display import Display

      #Display(13) instantiates a 13x13
      go = Display()    
  ```

### Place black and white stones:
  ```py
      go.place_stone(2, 3, "white")
      go.place_stone(7, 7, "black")
      go.place_stone(7, 8, "white")
      go.place_stone(7, 6, "white")
      go.place_stone(8, 7, "white")
  ```

### Query cell information (stone color, liberties, etc.):
  ```py
      go.state[7][7].color 
      #> 'black'
      
      go.state[7][7].liberties 
      #> {'east': 'white', 'north': None, 'south': 'white', 'west': 'white'}
      
      go.state[0][0].liberties
      #> {'east': None, 'north': 'edge', 'south': None, 'west': 'edge'}
      
      go.state[8][7].N
      #> 'black'
  ```
