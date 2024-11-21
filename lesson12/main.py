"""
Lesson 12: Combining lists
"""

# Write a function that concatenates two lists and returns
# the resulting list. For example:
# ["a","b","c"], [1,2,3] → ["a","b","c",1,2,3]

def coconut(x, y):
    #THIS X COCONUT WILL MUTATE
    # for i in range(len(y)):
    #     x.append(y[i])
    return x+y
# Write a function that combines two lists by alternatingly
# taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].
# If the length of the lists is not the same, raise a ValueError
def combine(x, y):
    if not len(x) == len(y):
        raise ValueError()
    z = []
    for i in range(len(x)):
          z.append(x[i])
          z.append(y[i])
    return z

# Extra: Write a function that merges two sorted lists into a
# new sorted list. For example,
# [1,4,6],[2,3,5] → [1,2,3,4,5,6]      
def norder(x, y):
    i = 0
    j = 0
    z = []
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            z.append(x[i])
            i += 1
        else: 
            z.append(y[j])
            j += 1
    if i == len(x):
        for jj in range(j, len(y)):
            z.append(y[jj])
    else:
        for ii in range(i, len(x)):
            z.append(x[ii])
    
    return z

if __name__ == "__main__":
    fdsa = norder([1, 1, 3], [2, 2, 4, 5])
    print(fdsa)