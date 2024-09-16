"""

Note the piece has access to the grid containing the piece,
since it's each piece's responsibility to check where it can
move.
"""
from enum import Enum
from location import Location

class Side(Enum):
    """
    Number indicates terminal color code for piece representation
    """
    BLACK = 36
    WHITE = 31

class PieceKind(Enum):
    ROOK = "R"
    KNIGHT = "N"
    BISHOP = "B"
    KING = "K"
    QUEEN = "Q"
    PAWN = "p"

PIECE_IDS = {
    "R": PieceKind.ROOK,
    "N": PieceKind.KNIGHT,
    "B": PieceKind.BISHOP,
    "K": PieceKind.KING,
    "Q": PieceKind.QUEEN,
    
    # NOTE: pawn is omitted, as it's represented specially
    # "": PieceKind.PAWN
}

class Piece:
    def __init__(self, encoded_piece: str, grid: "Grid"):
        """
        `encoded_piece` should be a string of format
        "<loc>,<PIECE_ID>,<side>" For example, a black pawn
        on A2 should be represented as "a2,P,B". Raises an
        error if the piece cannot be decoded.

        Note: "Grid" is given as a string to give a type hint
        without introducing a circular dependency. 
        """
        self.grid = grid

        loc, piece_id, side = encoded_piece.strip().split(",")
        file = loc[0]
        rank = int(loc[1])
        self.location = Location(file, rank)
        if piece_id == "P":
            self.kind = PieceKind.PAWN
        elif piece_id in PIECE_IDS:
            self.kind = PIECE_IDS.get(piece_id)
        else:
            raise ValueError(f"Invalid piece ID '{piece_id}'")

        if side == "B":
            self.side = Side.BLACK
        elif side == "W":
            self.side = Side.WHITE
        else:
            raise ValueError(f"Invalid side '{side}'")
       
        self.grid.set(self.location, self) 

    def get_pretty(self):
        color = self.side.value
        return f"\033[1;{color}m{self.kind.value}\033[0;37;0m"
