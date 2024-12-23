import random
import time

def init(n):
    grid = []
    for i in range(n):
        temporary = []
        for j in range(n):
            temporary.append(random.choice(["🔲", "⬛"]))
        grid.append(temporary)
    return grid
        #[[🔲, 🔲], [🔲, 🔲]]

def display(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            print(grid[i][j], end = "")
        print()

def life(grid):
    newgrid = []
    for l in range(len(grid)):
        temporary2 = []
        for ll in range(len(grid[0])):
            temporary2.append("⬛")
        newgrid.append(temporary2)

    for ii in range(len(grid)):
        for jj in range(len(grid[0])):
            container = liveneighbors(grid, ii, jj)
            if container == 3:
                newgrid[ii][jj] = "🔲"
            if container == 2:
                newgrid[ii][jj] = grid[ii][jj]
            if container >= 4 or container <= 1:
                newgrid[ii][jj] = "⬛"
            
    return newgrid

def liveneighbors(grid, i, j):
    livecount = 0
    livecount += alive(grid, i-1, j-1)
    livecount += alive(grid, i-1, j)
    livecount += alive(grid, i-1, j+1)
    livecount += alive(grid, i, j+1)
    livecount += alive(grid, i, j-1)
    livecount += alive(grid, i+1, j-1)
    livecount += alive(grid, i+1, j)
    livecount += alive(grid, i+1, j+1,)
    return livecount

def alive(grid, i, j):
    if len(grid) > i and i >= 0:
        if len(grid[i]) > j and j >= 0:
            if grid[i][j] == "🔲":
                return 1
    return 0


if __name__ == "__main__":
    grid = init(10)
    while True:
        display(grid)
        time.sleep(1)
        print()
        grid = life(grid)