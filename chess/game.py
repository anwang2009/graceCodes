from grid import Grid
from piece import Side
import sys


if __name__ == "__main__":
    g = Grid()
    g.display()
   
    side = Side.WHITE
    while True:
        next_move = input(f"\033[0;{side.value}mNext move:\033[0;37;0m ") 
        g.move(next_move)
        g.display()
        sys.exit()
