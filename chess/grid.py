"""
An 8x8 grid to represent a chess board
"""
import os
from location import Location
from piece import Piece

PIECES_FILE = os.path.join(os.path.dirname(__file__), "pieces.txt")

"""
The grid contains locations from A to H, 1 to 8 inclusive. 
If there is no piece at a location on the grid, the value will be None.
"""
class Grid:
    def __init__(self):
        # row, col
        self.grid = [[None for _ in range(8)] for _ in range(8)]

        self._load_pieces(PIECES_FILE)

    def get(self, loc: str):
        """
        Gets the piece at location loc.
        """
        pass

    def set(self, loc: Location, piece: Piece):
        """
        Sets the piece at location loc.
        """
        self.grid[loc.row][loc.col] = piece

    def move(self, command: str):
        """
        Moves a piece according to the given command. The command
        should be in standard chess notation. If the command indicates
        an invalid move for any reason, raises an error.

        Note, if two pieces can move to the same spot, the file takes
        precedence over the rank.
        """
        if "x" in command:
            # Piece takes piece
            src, dest = command.split("x")
            dest_loc = Location(dest[0], dest[1])
           
            # Get source piece somehow 
        else:
            pass

    def _load_pieces(self, pieces_file: str):
        """
        Loads pieces specified in the `pieces_file` at their
        specified locations in the grid.
        """
        with open(pieces_file) as f:
            for line in f.readlines():
                piece = Piece(line.strip(), self)

    def display(self):
        """
        Displays the grid
        """
        rows = []
        rows.append("    A   B   C   D   E   F   G   H")

        for i in range(7, -1, -1):
            rows.append(   "   --- --- --- --- --- --- --- ---")
            next_row = f"{i} |   |   |   |   |   |   |   |   | {i}"
            next_row = f"{i} | "
            for j in range(8):
                next_piece = self.grid[i][j]
                if next_piece is None:
                    next_row += "  | "
                else:
                    piece_rep = next_piece.get_pretty()
                    next_row += f"{piece_rep} | "

            next_row += str(i)
            rows.append(next_row)

        rows.append(   "   --- --- --- --- --- --- --- ---")
        rows.append("    A   B   C   D   E   F   G   H")

        for row in rows:
            print(row)

