"""
A location in standard chess notation is given by a file (A-H)
and a rank (1-8).
"""
class Location:
    def __init__(self, file: str, rank: int):
        self.file = file
        self.rank = rank

        if len(file) != 1:
            raise ValueError(f"Invalid location file given: {file}")

        # Calculate the ASCII value of the single character 
        ord_file = ord(file.lower())
        col = ord_file - ord('a')

        if col < 0 or col >= 8:
            raise ValueError(f"Invalid location file given: {file}")

        self.col = col

        if self.rank < 1 or self.rank > 8:
            raise ValueError(f"Invalid location rank given: {rank}")

        self.row = 8 - (self.rank)

    
