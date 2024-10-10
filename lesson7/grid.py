"""
Lesson 7: Representing 2D grids
"""

# How would you represent a 2D grid in Python?
# Assume each spot in the grid is either empty or "X".
def grid(rows, columns):
    X = "X"
    blank = "."
    for i in range(rows): #Rows
        for j in range(columns): #Stuff in lines for odd rows
            if (i+j) % 2 == 0: #odd
                print(X, end="")
            else: #even
                print(blank, end="")
        print()
# How would you print out the 2D grid?

# Code it with a main function
if __name__ == "__main__":
    grid(4, 4)
