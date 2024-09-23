"""
Lesson 3 extra control flow
"""

# TODO (2): Create a function that has no arguments
# that prints "Hello world!" when called.
def greeting():
    print("Hello World!")

# TODO (3): Create a function that has no arguments
# that introduces yourself when called.
def introduction():
    print("I am Grace!")

# TODO (4): Create a function that has one integer argument
# that does the following:
# If we list all the natural numbers below 10 that
# are multiples of 3 or 5, we get 3, 5, 6, 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5
# below the provided argument n. Return this sum.
def multiples_sum(n):
    addon = 0
    for i in range(1, n):
        if i % 3 == 0:
            addon += i
        if i % 5 == 0:
            addon += i
    return addon


# TODO (5): Create a function that takes one string argument.
# The provided argument will be a name. When called the
# function should print "Good job, An!" if called with "An". 
def takearg(name):
    # name = input("What is your name?: ")
    print("Good job,", name)

# TODO (6): Create a function that takes two integer arguments
# x and y. The function should return the minimum of the two
# arguments. 
def lesser(x, y):
    if x <= y:
        return x
    else:
        return y



# TODO (1): How do you define a "main" function (the desired 
# entry point of a script) in python? You can refer to past
# files for examples of this.
# 
# In Java, main looks like:
#    public static void main(String args[]) {}
# In C, main looks like either of the following:
#    int main() {}
#    int main(int argc, char* argv[]) {}
if __name__ == "__main__":
    greeting()
    introduction()
    value = multiples_sum(10)
    print(value)
    takearg("An")
    value2 = lesser(11, 10)
    print(value2)
# 
# Your completed main function should call the functions
# you define in the other TODOs.
#    2. Call the function
#    3. Call the function
#    4. Call the function with argument 1000 and print the result
#    5. Call the function with argument "Grace"
#    6. Call the function with arguments 2 and 3 and print the result

