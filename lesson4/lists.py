"""
Lesson 4: iterating over lists
"""

def print_even_index(stuff: list):
    print("[", end='')

    for i in range(0, len(stuff), 2):
        if i + 2 < len(stuff):
            print(str(stuff[i]) + ",", end=" ")
        else:
            print(stuff[i], end="")
    
    print("]", end='')


def my_print(stuff: list):
    print("[", end='')
    # TODO: print the list of "stuff" with semicolons instead of commas
    for i in range(0, len(stuff)):
        if i + 1 < len(stuff):
            print(str(stuff[i]) + ";", end=" ")
        else:
            print(stuff[i], end="")
    print("]", end='')


def reverse(stuff: list):
    # TODO: return a list that has all the elements in `stuff`
    # in reverse order
    result = []
    for i in range(len(stuff) - 1, -1, -1):
        item = stuff
        result.append(item[i])
    return result

def sum(stuff: list):
    result = 0
    for num in stuff:
        result += num

    return result


def multiply(stuff: list):
    # TODO: implement this
    result = 1
    for num in stuff:
        result *= num

    return result


def main():
    nums = [2, 3, 4, 5, 6, 10]

    # add and multiply nums
    print("sum of nums is", sum(nums))
    print("multiply of nums is", multiply(nums))

    # printing nums
    print("print(nums) is", nums)

    print("printing every even index of nums: ", end='')
    print_even_index(nums)
    print()

    print("my_print(nums) is ", end='')
    my_print(nums)
    print()

    # operations on nums
    print("reverse of nums is ", reverse(nums))


if __name__ == "__main__":
    main()
