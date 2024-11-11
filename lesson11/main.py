"""
Lesson 11: Guessing game
"""
import random


def min(nums):
    # Warmup: return the minimum number in the list of numbers
    another = nums[0]
    for i in range(len(nums)):
        if nums[i] < another:
            another = nums[i]
    return another


def index_min(nums):
    # Warmup: return the index of the minimum number in the list of numbers
    numsnumber = nums[0]
    index = None
    for i in range(len(nums)):
        if nums[i] <= numsnumber:
            index = i
            numsnumber = nums[i]
    return index



def game():
    # Implement a guessing game, where the user has to guess a number between
    # 1 and 100. Print "higher" or "lower" when the user guesses wrong, until
    # they get the right answer!
    target = random.randint(1, 100)
    while True:
        guessed = int(input("Guess a number between 1 and 100:"))
        print(guessed)
        if guessed < target:
            print("Wrong! This number is greater than", guessed)
        elif guessed > target:
            print("Wrong! This answer is less than", guessed)
        else:
            print("Correct! Good game!")
            break
    
    

if __name__ == "__main__":
    # your stuff here
    game()