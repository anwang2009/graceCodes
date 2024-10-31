# Lesson 9: Loop practice

def exercise01():
    # TODO: print the first 10 natural numbers using a while loop
    nat = 0
    while nat < 10:
        print(nat)

        nat += 1


def exercise02():
    # TODO: write a program to print the following number pattern
    # using a loop:
    # 1
    # 1 2
    # 1 2 3
    # 1 2 3 4
    # 1 2 3 4 5
    for i in range(1, 6):
        print(1, end=" ")
        if i > 1:
            print(2, end=" ")
            if i > 2:
                print(3, end=" ")
                if i > 3:
                    print(4, end=" ")
                    if i > 4:
                        print(5, end=" ")
        print()
def excercise02b():
    for i in range(1, 6):
        for j in range(1, i+1):
            print(j, end = " ")
        print()

def exercise03(y):
    # TODO: Calculate the sum of all numbers from 1 to a given number.
    # Get the number from user input and print the sum
    print(y * (1+y)//2)
def exercise03b(y):
    agh = 0
    for i in range(y+1):
        agh = agh + i
    print(agh)


def exercise04(n):
    # TODO: Print the multiplication table up to and including 10 of a given number.
    # Get the number from user input.
    for i in range(1, 11):
        print(n * i)

def exercise05():
    # TODO: Print numbers that are divisible by 5 and less than or equal to 150.
    # from the list below. If the number is greater than 500, stop the loop.
    numbers = [12, 75, 150, 180, 145, 525, 50]
    for i in range(len(numbers)):
        if numbers[i] <= 150:
            if numbers[i] % 5 == 0:
                print(numbers[i])
        elif numbers[i] > 500:
            break

if __name__ == "__main__":
    # Every time you finish an exercise, modify the following
    # function call to see if the output is correct.
 exercise05()
