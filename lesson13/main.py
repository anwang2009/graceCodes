"""
Lesson 13: 2D arrays
"""

# Warmup: Write a function that prints the first n prime numbers, where n
# is given as an argument
def isprime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

def printprimes(n):
    for i in range(1, n+1):
        if isprime(i):
            print(i)

def printmanyprimes(n):
    primesuspect = 0
    while n > 0:
        if isprime(primesuspect):
            n -= 1
            print(primesuspect)
        primesuspect += 1
        

# Write a function "init_2D" that constructs and returns a list that contains three lists.
# Each inner list has three numbers. Each number from 1 to 9 inclusive should be
# represented.
def init_2D():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    big = [a, b, c]
    return big

# Write a function "print_2D" that displays a given argument "list2D".
# Python will print [['x', 'y', ['x','y'], ['x', 'y']] as [[x, y], [x, y], [x, y]] but
# we want the output
# xy
# xy
# xy
def print_2D(list2D):
    for i in range(len(list2D)):
        for j in range(len(list2D[i])):
            if len(list2D)-1 == j:
                print(list2D[i][j])
            else:
                print(list2D[i][j], end = "")
    
if __name__ == "__main__":
    fdsa = init_2D()
    print_2D(fdsa)