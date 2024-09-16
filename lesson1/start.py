"""
Lesson 1: simple functions
"""


def times_three(x: int):
    return x * 3


def add(x: int, y: int):
    return x + y


def times_two(x: int):
    # TODO
    raise NotImplementedError()


def multiply(x: int, y: int):
    # TODO
    raise NotImplementedError()


def power2(x: int):
    return x * x


def power3(x: int):
    # TODO
    raise NotImplementedError()


if __name__ == "__main__":
    print("times three of 2 is", times_three(2))
    print("times two of 2 is", times_two(2))

    print("add of 2 and 3 is", add(2, 3))
    print("multiply of 2 and 3 is", multiply(2, 3))
    
    print("3 to the second power is", power2(3))
    print("3 to the third power is", power3(3))

