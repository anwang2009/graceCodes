"""
Lesson 6: Boolean expressions
"""


def check(expression_str, actual_result, expected):
    message = f"{expression_str} evaluates to {actual_result}"
    if actual_result == expected:
        prefix = "GOOD JOB!"
    else:
        prefix = "HMM TRY AGAIN!"

    print(prefix, message)


def run_boolean_exprs():
    x = 12
    y = 7
    z = 28
    s = "hi grace"

    check("x < 14",                        x < 14,                        True)
    check("x % 2 < 1",                     x % 2 < 1,                     True)
    check("x < y or x < z",                x < y or x < z,                True)
    check("y < x and x < z",               y < x and x < z,               True)
    check("z / x < x / y * x",             z / x < x / y * x,             True)
    check("len(s) == y",                   len(s) == y,                   False)
    check('s == "hi grace" or x * y != z', s == "hi grace" or x * y != z, True)



def foo(x, y):
    """
    TODO:
    Is the assertion z == 0 at each of the points always, never, or sometimes True?
    Write a test case demonstrating full coverage of all the possible code branches.

    A: Always true, because nothing happens to z, nothing interacts or checks z. Z is simply 0 according to line 46
    B: SOMETIMES, because repeats.
    C: Never true, because after line 51, z is not 0 anymore, but rather 1
    D: Never true, because after line 51, z is not 0 anymore, but rather 1
    E: SOMETIMES, because if we skip all the "if-else," then we show up with z=0, and not a z+=1 with the ifs
    """


    z = 0

    print("a", z)# Point A
    while x != y:
        print("b", z)# Point B
        z += 1

        if (x > y):
            print("c", z)# Point C
            x = x // 10
        else:
            print("d", z)# Point D
            y = y // 10

    print("E", z)# Point E
    print(str(x) + " " + str(y) + " " + str(z))


if __name__ == "__main__":
    run_boolean_exprs()
    foo(1, 0)
    print("test")
    foo(3, 0)
    print("test")
    foo(10, 0)
    print("test")
    foo(0, 1)
    print("test")
    foo(0, 3)
    print("test")
    foo(0, 0)