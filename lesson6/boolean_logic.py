"""
Lesson 6: Boolean expressions
"""


def check(expression_str, actual_result, expected):
    message = f"{expression_str} evaluates to {actual_result}"
    if actual_result == expected:
        prefix = "GOOD JOB!"
    else:
        prefix = "HMM TRY AGAIN!"

    print(f"{prefix} {message}")


def run_boolean_exprs():
    x = 12
    y = 7
    z = 28
    s = "hi grace"

    check("x < 14",                        x < 14,                        True)
    check("x % 2 < 1",                     x % 2 < 1,                     """TODO""")
    check("x < y or x < z",                x < y or x < z,                """TODO""")
    check("z / x < x / y * x",             z / x < x / y * x,             """TODO""")
    check("len(s) == y",                   len(s) == y,                   """TODO""")
    check('s == "hi grace" or x * y != z', s == "hi grace" or x * y != z, """TODO""")



def foo(x, y):
    """
    TODO:
    Is the assertion z == 0 at each of the points always, never, or sometimes True?
    Write a test case demonstrating full coverage of all the possible code branches.

    A:
    B:
    C:
    D:
    E:
    """


    z = 0

    # Point A
    while x != y:
        # Point B
        z += 1

        if (x > y):
            # Point C
            x = x / 10;
        else:
            # Point D
            y = y / 10;

    # Point E
    print(x + " " + y + " " + z)


if __name__ == "__main__":
    run_boolean_exprs()

