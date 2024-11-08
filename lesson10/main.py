"""
Lesson 10: short functions
"""

def index_of(some_list, element):
   # This function should return the index of the first item
   # in the list that matches the given `element` argument.
   # If there are no items that equal `element,
   # return -1.
   for i in range(len(some_list)):
      if some_list[i] == element:
         return i
   return -1
   


def fibonacci(n):
   # This function should print the first n fibonacci numbers
   x = 1
   pastx = 0
   temporarystorage = pastx
   for i in range(n):
      print(x)
      temporarystorage = pastx
      pastx = x
      x = temporarystorage + x


if __name__ == "__main__":
    fdsa = index_of([1, 2, 3, 3, 5], 3)
    try:
        print([1, 2, 2, 3, 5].index(10))
    except Exception as e:
        print("Caught error", e)
    fibonacci(10)
    x = 5
    z = x
    y = 6
    x = y
    y = z
    print(x, y)